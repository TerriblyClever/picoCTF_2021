// These pesky special agents keep reverse engineering our source code and then
// breaking into our secret vaults. THIS will teach those sneaky sneaks a
// lesson.
//
// -Minion #0891
import java.util.*; 
import javax.crypto.Cipher; 
import javax.crypto.spec.SecretKeySpec;
import java.security.*; 


class VaultDoor8 {

    public static void main(String args[]) {
        /*
        Scanner b = new Scanner(System.in); 
        System.out.print("Enter vault password: ");
        String c = b.next(); 

        //creates a substring of 'c' (the password) starting at the 9th 
        //character and extending to the next to last character 
        //(c.length()-1)
        String f = c.substring(8,c.length()-1); 
        VaultDoor8 a = new VaultDoor8(); 
        */

        //Beginning of experimental area
        //System.out.println(a.scramble(c));
        VaultDoor8 a = new VaultDoor8(); 
        //char[] answer = {0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4, 0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86, 0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xD2, 0xD0, 0xB4, 0xE1, 0xC1, 0xE0, 0xD0, 0xD0, 0xE0 };
        //String string_answer = new String(answer);
        //String f = string_answer.substring(8,string_answer.length()-1); 
        
        String message = "ôÀðwÀäðw¤ÐÅwôÐ¥E'µwÒÐ´áÁàÐÐà";
        String unscrambled = a.unscramble("ôÀðwÀäðw¤ÐÅwôÐ¥E'µwÒÐ´áÁàÐÐà");
        System.out.println(unscrambled);

        //System.out.println(c);
        //System.out.println(f);
        //System.out.println();

        //End of experimental area
        
        /*
        if (a.checkPassword(f)) {
            System.out.println("Access granted."); 
        }
        else {
            System.out.println("Access denied!"); 
        } 
        */
    } 

    public char[] scramble(String password) {
        /* Scramble a password by transposing pairs of bits. */
        char[] a = password.toCharArray(); 
        for (int b=0; b<a.length; b++) { //for loop that runs the length of the char array made from 'password'
            char c = a[b]; //Creates a char variable 'c' equal to char array 'a' in position 'b', or the first byte, and then incremented
            c = switchBits(c,1,2);
            c = switchBits(c,0,3); 
            /* c = switchBits(c,14,3); 
            c = switchBits(c, 2, 0); */ 
            c = switchBits(c,5,6); 
            c = switchBits(c,4,7);
            c = switchBits(c,0,1); 
            /* d = switchBits(d, 4, 5); 
            e = switchBits(e, 5, 6); */ 
            c = switchBits(c,3,4); 
            c = switchBits(c,2,5); 
            c = switchBits(c,6,7); 
            a[b] = c; //replaces the contents of char array 'a' at position 'b' with the modified byte 'c'
        } 
        return a;
    }
    
    public char[] unscramble(String password) {
        /* Unscramble a string by running the bit scramble in revers. */
        char[] a = password.toCharArray(); 
        for (int b=0; b<a.length; b++) {
            char c = a[b]; 
            c = switchBits(c,6,7); 
            c = switchBits(c,2,5); 
            c = switchBits(c,3,4); 
            c = switchBits(c,0,1); 
            c = switchBits(c,4,7);
            c = switchBits(c,5,6); 
            c = switchBits(c,0,3); 
            c = switchBits(c,1,2); //Last line to move
            /* c = switchBits(c,14,3); 
            c = switchBits(c, 2, 0); */ 
            /* d = switchBits(d, 4, 5); 
            e = switchBits(e, 5, 6); */ 
            a[b] = c; 
        } 
        return a;
    } 

    public char switchBits(char c, int p1, int p2) {
        /* Move the bit in position p1 to position p2, and move the bit
        that was in position p2 to position p1. Precondition: p1 < p2 */ 
        //creates a char type variable 'mask1' that is typecast (char) the result of (1<<p1)
        char mask1 = (char)(1 << p1); //'<<' is a bitwise operator and shifts the bits of the number to the left the specified number of positions
        char mask2 = (char)(1 << p2); 
        /* char mask3 = (char)(1<<p1<<p2); 
        mask1++; mask1--; */ 
        //copies a bit into the result if it exists in both operands
        char bit1 = (char)(c & mask1); 
        char bit2 = (char)(c & mask2); 
        /* System.out.println("bit1 " + Integer.toBinaryString(bit1));
        System.out.println("bit2 " + Integer.toBinaryString(bit2)); */ 
        char rest = (char)(c & ~(mask1 | mask2)); 
        char shift = (char)(p2 - p1); 
        char result = (char)((bit1<<shift) | (bit2>>shift) | rest); 
        return result;
    } 

    public boolean checkPassword(String password) {
        char[] scrambled = scramble(password); 
        char[] expected = {
            0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 
            0xC0, 0xE4, 0xF0, 0x77, 0xA4, 0xD0, 
            0xC5, 0x77, 0xF4, 0x86, 0xD0, 0xA5, 
            0x45, 0x96, 0x27, 0xB5, 0x77, 0xD2, 
            0xD0, 0xB4, 0xE1, 0xC1, 0xE0, 0xD0, 
            0xD0, 0xE0 };
        return Arrays.equals(scrambled, expected); 
    } 
}