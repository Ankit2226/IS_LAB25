import java.math.BigInteger;
import java.security.SecureRandom;

public class DiffieHellman {

    private BigInteger privateKey;
    private BigInteger publicKey;
    private BigInteger sharedSecret;
    
    private static final BigInteger g = new BigInteger("2"); // Generator
    private static final BigInteger p = new BigInteger("23"); // Prime number

    public DiffieHellman() {
        // Generate private key
        SecureRandom random = new SecureRandom();
        this.privateKey = new BigInteger(64, random);
        
        // Calculate public key
        this.publicKey = g.modPow(privateKey, p);
    }

    public BigInteger getPublicKey() {
        return publicKey;
    }

    public void generateSharedSecret(BigInteger otherPublicKey) {
        // Calculate shared secret using the other party's public key
        this.sharedSecret = otherPublicKey.modPow(privateKey, p);
    }

    public BigInteger getSharedSecret() {
        return sharedSecret;
    }

    public static void main(String[] args) {
        // User A
        DiffieHellman userA = new DiffieHellman();
        System.out.println("User A's public key: " + userA.getPublicKey());

        // User B
        DiffieHellman userB = new DiffieHellman();
        System.out.println("User B's public key: " + userB.getPublicKey());

        // Generate shared secrets
        userA.generateSharedSecret(userB.getPublicKey());
        userB.generateSharedSecret(userA.getPublicKey());

        // Display shared secrets
        System.out.println("User A's shared secret: " + userA.getSharedSecret());
        System.out.println("User B's shared secret: " + userB.getSharedSecret());
    }
}
