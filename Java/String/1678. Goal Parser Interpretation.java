class Solution {
    public String interpret(String command) {
        // command = command.replace("()","o");
        // command = command.replace("(al)","al");
        // return command;
        String result = "";
        for(int i = 0; i<command.length(); i++){
            if(command.charAt(i)== 'G'){
                result += "G";
            }
            if(command.charAt(i)=='(' && command.charAt(i+1)==')'){
                result += "o";
            }
            if(command.charAt(i)=='(' && command.charAt(i+1)=='a'){
                result += "al";
            }
        }
        return result;
    }
}