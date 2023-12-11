// Jose Alfonzo 17-10012

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class ProductoPunto {
    public static void main(String[] args) {
        // Vectores a los que le aplicaremos el producto punto
        int[] vector1 = {1, 2, 3, 4, 5};
        int[] vector2 = {6, 7, 8, 9, 10};
        int n = vector1.length;
        // Variable que almacena el numero de hilos
        int numThreads = Runtime.getRuntime().availableProcessors();
        // Variable que almacena una instancia de  ExecutorService para crear y manejar hilos
        ExecutorService executor = Executors.newFixedThreadPool(numThreads);
        int[] results = new int[numThreads];
        for (int i = 0; i < numThreads; i++) {
            int start = i * n / numThreads;
            int end = (i + 1) * n / numThreads;
            executor.execute(new ProductoPuntoInterfaz(vector1, vector2, start, end, results, i));
        }
        executor.shutdown();
        while (!executor.isTerminated()) {
            Thread.yield();
        }
        int product = 0;
        for (int i = 0; i < numThreads; i++) {
            product += results[i];
        }
        // Imprimimos el resultado
        System.out.println("El producto punto es: " + product);
    }
}
// Usamos runnable
class ProductoPuntoInterfaz implements Runnable {
    // Creamos las variables
    private final int[] vector1;
    private final int[] vector2;
    private final int start;
    private final int end;
    private final int[] results;
    private final int index;

    public ProductoPuntoInterfaz(int[] vector1, int[] vector2, int start, int end, int[] results, int index) {
        // Creamos las variables
        this.vector1 = vector1;
        this.vector2 = vector2;
        this.start = start;
        this.end = end;
        this.results = results;
        this.index = index;
    }
    @Override
    public void run() {
        // Creamos la variable que tendra la respuesta
        int result = 0;
        for (int i = start; i < end; i++) {
            result += vector1[i] * vector2[i];
        }
        results[index] = result;
    }
}
