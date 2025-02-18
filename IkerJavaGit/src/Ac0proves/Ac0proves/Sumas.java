package Ac0proves;

import java.util.Scanner;

public class Sumas {
    public static void main(String[] args) {
        Scanner sumes = new Scanner(System.in);

        System.out.println("Posa un numero: ");
        int numero1 = sumes.nextInt();

        System.out.println("Posa un numero: ");
        int numero2 = sumes.nextInt();

        int suma = numero1 + numero2;

        System.out.println("Suma: " + suma);
    }
}
