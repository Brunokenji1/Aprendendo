import java.io.IOException;
import java.util.Scanner;

public class problema {
        public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] num = new int[n];
        

        for(int i=0; i<n; i++){
            num[i]=sc.nextInt();
        }

        if(n<=2){
            System.out.println("1");
        }
        
        else{
            int qtd=1;
            int diferenca=num[1]-num[0];
            for(int i=2; i<n; i++){
                int ultimoDif=num[i]-num[i-1];
                if(ultimoDif!=diferenca){
                    qtd++;
                    diferenca=ultimoDif;
                }
            }
            System.out.println(qtd);
        }
        sc.close();
        

    }
}
