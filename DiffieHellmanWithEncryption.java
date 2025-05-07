import java.math.BigInteger;
import java.util.Scanner;

public class DiffieHellmanWithEncryption {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

       
        System.out.print("Enter prime number (p): ");
        BigInteger p = new BigInteger(sc.next());

        System.out.print("Enter primitive root (g): ");
        BigInteger g = new BigInteger(sc.next());

        System.out.print("Enter Alice's private key (a): ");
        BigInteger a = new BigInteger(sc.next());

        System.out.print("Enter Bob's private key (b): ");
        BigInteger b = new BigInteger(sc.next());

       
        BigInteger A = g.modPow(a, p);  
        BigInteger B = g.modPow(b, p); 

       
        BigInteger sharedSecret = B.modPow(a, p);  

        System.out.println("\nShared Secret: " + sharedSecret);

       
        System.out.print("\nEnter message to encrypt (uppercase letters only): ");
        sc.nextLine(); 
        String message = sc.nextLine().toUpperCase();

        int shift = sharedSecret.mod(BigInteger.valueOf(26)).intValue();  // keep within alphabet
        String encrypted = encrypt(message, shift);
        String decrypted = decrypt(encrypted, shift);

        
        System.out.println("\nEncrypted Message: " + encrypted);
        System.out.println("Decrypted Message: " + decrypted);

        sc.close();
    }

  
    private static String encrypt(String msg, int shift) {
        StringBuilder sb = new StringBuilder();
        for (char ch : msg.toCharArray()) {
            if (Character.isUpperCase(ch)) {
                char enc = (char) ((ch - 'A' + shift) % 26 + 'A');
                sb.append(enc);
            } else {
                sb.append(ch); 
            }
        }
        return sb.toString();
    }

    
    private static String decrypt(String msg, int shift) {
        StringBuilder sb = new StringBuilder();
        for (char ch : msg.toCharArray()) {
            if (Character.isUpperCase(ch)) {
                char dec = (char) ((ch - 'A' - shift + 26) % 26 + 'A');
                sb.append(dec);
            } else {
                sb.append(ch);
            }
        }
        return sb.toString();
    }
}
