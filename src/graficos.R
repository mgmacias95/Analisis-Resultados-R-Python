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

# PRACTICA 1
# datos_p1 <- construye_datos(resultados = c("resultados_localsearch.csv","resultados_simulatedannealing.csv",
#     "resultados_tabubasic.csv", "resultados_tabuext.csv"), nombres=c("CosteLocalSearch", 
#     "TiempoLocalSearch", "DesvLS", "CosteSA", "TiempoSA", "DesvSA", "CosteTabuBasica", 
#     "TiempoTabuBasica", "DesvTB", "CosteTabu", "TiempoTabu", "DesvT"))
# representa_datos(datos=datos_p1, cols=c(1,2,3,6,9,12,15), nombres=c("Coste Local Search", 
#     "Coste Simulated Annealing", "Coste Tabú Básica", "Coste Tabú"), file="p1")

# PRACTICA 2
# datos_p2 <- construye_datos(resultados = c("resultados_multiarranquebasica.csv",
#     "resultados_grasp.csv", "resultados_ils.csv"), nombres=c("CosteMultBasica", 
#     "TiempoMultBasica", "DesvMultB", "CosteGrasp", "TiempoGrasp", "DesvGrasp", 
#     "CosteIls", "TiempoIls", "DesvIls"))
# representa_datos(datos=datos_p2, cols=c(1,2,3,6,9,12), nombres=c("Coste Multiarranque Básica",
#     "Coste GRASP", "Coste ILS"), file="p2")
# print(representa_convergencia(resultados=c("conver_grasp.csv","conver_ils.csv",
#     "conver_mb.csv"), nombres=c("Iteraciones", "GRASP", "ILS", "MB"), file="p2"))

# PRACTICA 3 
# datos_p3 <- construye_datos(resultados = c("resultados_EAGEP.csv","resultados_EAGEX.csv",
#     "resultados_EAGGP.csv", "resultados_EAGGX.csv"), nombres=c("CosteAGEP", 
#     "TiempoAGEP", "DesvAGEP", "CosteAGEX", "TiempoAGEX", "DesvAGEX", 
#     "CosteAGGP", "TiempoAGGP", "DesvAGGP", "CosteAGGX", "TiempoAGGX", "DesvAGGX"))
# representa_datos(datos=datos_p3, cols=c(1,2,3,6,9,12,15), nombres=c("Coste AGEP",
#     "Coste AGEX", "Coste AGGP", "Coste AGGX"), file="p3")
# representa_convergencia(resultados=c("conver_AGEP.csv","conver_AGEX.csv",
#     "conver_AGGP.csv", "conver_AGGX.csv"), nombres=c("Evaluaciones", "AGEP","AGEX","AGGP", 
#     "AGGX"), file="p3")

# # PRACTICA 4
# datos_p4 <- construye_datos(resultados = c("resultados_SCH.csv","resultados_SHMM.csv"),
#     nombres = c("CosteSCH", "TiempoSCH", "DesvSCH","CosteSHMM", "TiempoSHMM", "DesvSHMM"))
# representa_datos(datos=datos_p4, cols=c(1,2,3,6,9), nombres=c("Coste SCH", "Coste SHMM"),
#     file="p4")
# representa_convergencia(resultados=c("conver_SCH.csv","conver_SHMM.csv"), 
#     nombres=c("Evaluaciones", "SCH", "SHMM"), file="p4")

# PRACTICA 5
datos_p5 <- construye_datos(resultados = c("resultados_EM1.csv","resultados_EM2.csv", "resultados_EM3.csv"),
    nombres = c("CosteAM1", "TiempoAM1", "DesvAM1","CosteAM2", "TiempoAM2", "DesvAM2", "CosteAM3", "TiempoAM3", "DesvAM3"))
representa_datos(datos=datos_p5, cols=c(1,2,3,6,9,12), nombres=c("Coste AM(10,1.0)", "Coste AM(10, 0.1)", "Coste AM(10, 0.1mej)"),
    file="p5")
representa_convergencia(resultados=c("conver_M1.csv","conver_M2.csv","conver_M3.csv"), 
    nombres=c("Evaluaciones", "AM(10,1.0)", "AM(10,0.1)", "AM(10,0.1mej)"), file="p5")