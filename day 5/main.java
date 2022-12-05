import java.io.*;
import java.util.*;

class main {

    public static void main(String[] args){
        Vector<Stack<String>> stacks = new Vector<Stack<String>>();
        String[][] elementsArray = {{"D","M","S","Z","R","F","W","N"},{"W","P","Q","G","S"},{"W","R","V","Q","F","N","J","C"},{"F","Z","P","C","G","D","L"},{"T","P","S"},{"H","D","F","W","R","L"},{"Z","N","D","C"},{"W","N","R","F","V","S","J","Q"},{"R","M","S","G","Z","W","V"}};
        
        for(String[] elements : elementsArray){
            Stack<String> s1 = new Stack<String>();
            for(String element : elements){
            s1.push(element);
            }
            stacks.addElement(s1);
        }


        try  
        {  
            FileInputStream input=new FileInputStream("input.txt");       
            Scanner sc=new Scanner(input);    
            
            while(sc.hasNextLine())  
            {  
                String[] result = sc.nextLine().split("\\s");
                Stack<String> temp = new Stack<String>();
                for(int i = 0; i < Integer.parseInt(result[1]); i++){
                    temp.push(stacks.elementAt(Integer.parseInt(result[3])-1).pop());
                }
                for(int i = 0; i < Integer.parseInt(result[1]); i++){
                    try{
                        stacks.elementAt(Integer.parseInt(result[5])-1).push(temp.pop());
                        //stacks.elementAt(Integer.parseInt(result[5])-1).push(Integer.parseInt(result[3])-1).pop()); part 1
                    }catch(Exception e){
                        System.out.println("test");
                    }
                    
                }
            }  
            sc.close();
        }
        catch(IOException e)  
        {  
            e.printStackTrace();  
        }
        for(Stack<String> element : stacks){
            System.out.print(element.pop());
        }
    }

}