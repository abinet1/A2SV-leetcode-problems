class Solution {
    public int maxCoins(int[] piles) {
        Arrays.sort(piles);

        // System.out.println(Arrays.toString(piles));
        int sum = 0;
        for(int i=piles.length-2;i>=piles.length/3;i=i-2){
            sum = sum + piles[i];
        }
        return sum;
    }
}