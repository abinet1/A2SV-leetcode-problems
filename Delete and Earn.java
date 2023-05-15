import java.util.Stack;

class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] result = new int[temperatures.length];
        Stack<Integer> stack = new Stack<Integer>();
        Stack<Integer> stack_index = new Stack<Integer>();
        for(int i=0;i<temperatures.length;i++){
            while(stack.size()>0){
                // System.out.println(stack.peek());
                // System.out.println(temperatures[i]);
                if(stack.peek()<temperatures[i]){
                    stack.pop();
                    int index = stack_index.peek();
                    stack_index.pop();
                    result[index] = i-index;
                }else{
                    break;
                }
            }
            stack.push(temperatures[i]);
            stack_index.push(i);
            // System.out.println(stack);
            // System.out.println(stack_index);
            
        }
        // for(int i=0;i<result.length;i++){
        //     System.out.println(result[i]);
        // }
        return result; 
    }
}