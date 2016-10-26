construye_datos <- function(resultados, nombres) {
    mejor <- read.csv('Resultados/mejor_csv.csv')
    greedy <- read.csv('Resultados/resultados_greedy.csv')
    algoritmos <- lapply(X=resultados, FUN=function(r) read.csv(paste("Resultados/", r, sep="")))
    d <- data.frame(cbind(mejor, greedy, algoritmos))
    names(d) <- c("Caso", "MejorCoste", "CosteGreedy", "TiempoGreedy", "DesvGreedy", nombres)
    d
}

representa_datos <- function(datos, cols, nombres, file) {
    library(ggplot2)
    library(reshape2)
    d_c <- data.frame(cbind(datos[,cols]))
    names(d_c) <- c("Caso", "Mejor Coste", "Coste Greedy", nombres)
    d_c$Caso = datos$Caso
    d_chr <- melt(d_c[grepl("chr2",datos$Caso),])
    names(d_chr)  <- c("Caso", "Algoritmo", "Coste")
    ggplot(d_chr, aes(Caso, Coste)) + geom_bar(aes(fill=Algoritmo), position="dodge", stat="identity")
    ggsave(paste("chr",file,".png",sep=""))
    d_tai <- melt(d_c[grepl("tai",datos$Caso),])
    names(d_tai) <- c("Caso", "Algoritmo", "Coste")
    ggplot(d_tai, aes(Caso, Coste)) + geom_bar(aes(fill=Algoritmo), position="dodge", stat="identity")
    ggsave(paste("tai",file,".png",sep=""))
}

representa_convergencia <- function(resultados, nombres, file) {
    library(ggplot2)
    library(reshape2)
    convergencias <- lapply(X=resultados, FUN=function(r) read.csv(paste("Resultados/",r,sep="")))
    c <- lapply(X=convergencias, FUN=function(conv) conv[[2]])
    d_c <- data.frame(convergencias[[1]][,1],c)
    names(d_c) <- nombres
    d_c
    d_cm <- melt(d_c, id.vars=nombres[1])
    names(d_cm) <- c(nombres[1], "Algoritmo", "Coste")
    if (nombres[1] == "Evaluaciones") 
        ggplot(d_cm, aes(Evaluaciones,Coste)) + geom_line(aes(color=Algoritmo))
    else
        ggplot(d_cm, aes(Iteraciones,Coste)) + geom_line(aes(color=Algoritmo))
    ggsave(paste("conver",file,".png", sep=""))
}


datos_prueba <- construye_datos(resultados = c("resultados_localsearch.csv"),
    nombres = c("CosteLS", "TiempoLS", "DesvLS"))
representa_datos(datos=datos_prueba, cols=c(1,2,3,6), nombres=c("Coste Local Search"), file="prueba")
# representa_convergencia(resultados=c("conver_M1.csv","conver_M2.csv","conver_M3.csv"), 
#     nombres=c("Evaluaciones", "AM(10,1.0)", "AM(10,0.1)", "AM(10,0.1mej)"), file="p5")