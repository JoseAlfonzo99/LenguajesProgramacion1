KC=	kotlinc
KFLAG=	-cp

all:	\
	Pregunta3.class \
	MainKt.class

Pregunta3.class: Pregunta3.kt
	$(KC) $(KFLAG) . Pregunta3.kt

MainKt.class: Main.kt 
	$(KC) $(KFLAG) . Main.kt

clean:
	rm -rf *.class META-INF
