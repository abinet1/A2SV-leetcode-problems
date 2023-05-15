import java.util.HashMap; // import the HashMap class
import java.util.ArrayList; // import the ArrayList class

class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        
        HashMap<Integer, Integer> a = new HashMap<Integer,Integer>();
        ArrayList<Integer> arrayList = new ArrayList<>();

        for(int i=0; i<nums2.length; i++){
            arrayList.add(nums2[i]);
            for(int j=0; j<arrayList.size();j++){
                if(arrayList.get(j)<nums2[i]){
                    a.put(arrayList.get(j),nums2[i]);
                    arrayList.remove(j);
                    j=j-1;
                }
            }
        }

        int[] result = new int[nums1.length];
        for (int i=0;i<nums1.length;i++){
            if(a.containsKey(nums1[i])){
                result[i]=a.get(nums1[i]);
            }else{
                result[i]=-1;
            }
        }

        return result;
        
    }
}