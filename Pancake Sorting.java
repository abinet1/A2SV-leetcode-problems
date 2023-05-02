import java.util.ArrayList;
import java.util.List;

class Solution {
    private int[] sort(int end_point, int[] arr ){
        int start = 0;
        while(start<end_point){
            int a = arr[start];
            arr[start] = arr[end_point];
            arr[end_point] = a;
            start=start+1;
            end_point=end_point-1;
        }
        return arr;
    } 

    public List<Integer> pancakeSort(int[] arr) {
        ArrayList<Integer> response=new ArrayList<>();
        for(int i=arr.length-1;i>-1;i--){
            int max_index = i;
            for(int j=i;j>-1;j--){
                if(arr[max_index]<arr[j]){
                    max_index = j;
                }
            }
            if (max_index!=i){
                sort(max_index,arr);
                sort(i,arr);
                response.add(max_index+1);
                response.add(i+1);
            }
        }
        return response;
    }
}

