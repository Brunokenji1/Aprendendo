import java.io.IOException;
import java.util.Scanner;

public class problemadois {
    public static void main(String[] args) throws IOException {
        
        Scanner sc = new Scanner(System.in);
        
        while(sc.hasNext()){
            String x = sc.next();
        
            String[] horario = x.split(":");
            int hora = Integer.parseInt(horario[0]);
            int min = Integer.parseInt(horario[1]);
        
            int horaMax=8;
            int minMax= horaMax*60;

            int tempoMin=(hora*60)+min+60;
            if(tempoMin>minMax){
               int atrasoMax = tempoMin-minMax;
                System.out.println("Atraso maximo: " + atrasoMax);
            }
            else{
               System.out.println("Atraso maximo: 0");
            }
            sc.close();
        }

    }
}

