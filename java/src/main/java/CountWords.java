import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Scanner;

/**
 * Created with IntelliJ IDEA.
 * User: magarwal
 * Date: 8/25/17
 * Time: 1:25 PM
 * To change this template use File | Settings | File Templates.
 */
public class CountWords {
    public static void main(String[] args){

        File f = new File("C:/Users/magarwal/Desktop/SW_Prep/Bootcamps.txt");
        Scanner s = null;
        try {
            s = new Scanner(f);
        } catch (FileNotFoundException e) {
            e.printStackTrace();  //To change body of catch statement use File | Settings | File Templates.
        }

        Map <String,Integer> word_count = new LinkedHashMap<String, Integer>();

        while(s.hasNext()){
            String word = s.next();
            int count;
            if (word_count.containsKey(word)){
                count = word_count.get(word);
                count = count + 1;
                word_count.put(word,count);
            }
            else{
                word_count.put(word,1);
            }
        }

        for(Map.Entry<String,Integer> mentry : word_count.entrySet()){
            System.out.println(mentry.getKey() + " : " + mentry.getValue());

        }


    }
}
