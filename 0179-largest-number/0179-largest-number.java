class Solution {
    public String largestNumber(int[] nums) {
        String[] arr = Arrays.stream(nums).mapToObj(String::valueOf).toArray(String[]::new);
        Arrays.sort(arr,(a,b) -> (b+a).compareTo(a+b));
        String result = String.join("",arr);
        if(result.charAt(0)=='0')return "0";
        return result;
    }
}