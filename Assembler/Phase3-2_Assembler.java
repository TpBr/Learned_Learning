package edu.uiowa.cs;

import java.util.*;



public class Phase3 {

    /* Translate each Instruction object into
     * a 32-bit number.
     *
     * tals: list of Instructions to translate
     *
     * returns a list of instructions in their 32-bit binary representation
     *
     */
    
    
    
    
 
    public static List<Integer> translate_instructions(List<Instruction> tals) {
        List<Integer> result = new LinkedList<Integer>();
        
        int binary = 0b00000000000000000000000000000000;
        
        
        for(int i = 0; i < tals.size(); i++){
            if(tals.get(i).instruction_id.equals(Instruction.ID.addiu)){
               
                binary = 0b001001;
             
                binary = binary << 26; 
                
                int rs = tals.get(i).rs;
                
                rs = rs << 21;
                
                binary = binary | rs;
                
                int rt = tals.get(i).rt;
                
                rt = rt << 16;
                
                binary = binary | rt;
                
                if((tals.get(i).immediate & 0x1000) == 0x1000){
                    int temp = Math.abs(tals.get(i).immediate - 0xFFFF);  

                    temp ^= 0xFFFF;
                temp = temp ^ 0b10000000000000000;
                    binary = binary | Math.abs(temp);

                }
                else{
                    binary = binary | Math.abs(tals.get(i).immediate);

                }
                result.add(binary);
                binary = 0b0;
            } 
            if(tals.get(i).instruction_id.equals(Instruction.ID.beq)){
               
                binary = 0b100;
             
                binary = binary << 26; 
                
                int rs = tals.get(i).rs;
                
                rs = rs << 21;
                
                binary = binary | rs;
                
                int rt = tals.get(i).rt;
                
                rt = rt << 16;
                
                binary = binary | rt;
                if((tals.get(i).immediate & 0x1000) == 0x1000){
                    int temp = Math.abs(tals.get(i).immediate - 0xFFFF);  

                    temp ^= 0xFFFF;
                temp = temp ^ 0b10000000000000000;
                    binary = binary | Math.abs(temp);

                }
                else{
                    binary = binary | Math.abs(tals.get(i).immediate);

                }
                result.add(binary);
                binary = 0b00000000000000000000000000000000;
                
        }
        
        
        if(tals.get(i).instruction_id.equals(Instruction.ID.bne)){
               
                binary = 0b101;

                binary = binary << 26; 

                int rs = tals.get(i).rs;
                
                rs = rs << 21;
                
                binary = binary | rs;

                int rt = tals.get(i).rt;
                
                rt = rt << 16;
                
                binary = binary | rt;

                if((tals.get(i).immediate & 0x1000) == 0x1000){
                
                int temp = Math.abs(tals.get(i).immediate - 0xFFFF);  
                temp = temp ^ 0xFFFF;
                temp = temp ^ 0b10000000000000000;
                    
                binary = binary | (temp);

                }
                else{
                    binary = binary | Math.abs(tals.get(i).immediate);

                }
                
                
                result.add(binary);
                binary = 0b00000000000000000000000000000000;
        }
        if(tals.get(i).instruction_id.equals(Instruction.ID.lui)){
               
                binary = 0b1111;
             
                binary = binary << 26; 
                
                int rs = tals.get(i).rs;
                
                rs = rs << 21;
                
                binary = binary | rs;
                
                int rt = tals.get(i).rt;
                
                rt = rt << 16;
                
                binary = binary | rt;
               if((tals.get(i).immediate & 0x1000) == 0x1000){
                    int temp = Math.abs(tals.get(i).immediate - 0xFFFF);  

                    temp ^= 0xFFFF;
                temp = temp ^ 0b10000000000000000;
                    binary = binary | Math.abs(temp);

                }
                else{
                    binary = binary | Math.abs(tals.get(i).immediate);

                }
                result.add(binary);
                binary = 0b00000000000000000000000000000000;
        }
        if(tals.get(i).instruction_id.equals(Instruction.ID.ori)){
               
                binary = 0b1101;
                binary = binary << 26; 
                
                int rs = tals.get(i).rs;
                
                rs = rs << 21;
                
                binary = binary | rs;

                int rt = tals.get(i).rt;
                
                rt = rt << 16;
                
                binary = binary | rt;

                if((tals.get(i).immediate & 0x1000) == 0x1000){
                    int temp = Math.abs(tals.get(i).immediate - 0xFFFF);  

                    temp ^= 0xFFFF;
                temp = temp ^ 0b10000000000000000;
                    binary = binary | Math.abs(temp);

                }
                else{
                    binary = binary | Math.abs(tals.get(i).immediate);

                }

                result.add(binary);
                binary = 0b00000000000000000000000000000000;
        }
        if(tals.get(i).instruction_id.equals(Instruction.ID.addu)){ 
                
                int rs = tals.get(i).rs;
                
                rs = rs << 21;
                
                binary = binary | rs;
                
                int rt = tals.get(i).rt;
                
                rt = rt << 16;
                
                binary = binary | rt;
                
                int rd = tals.get(i).rd;
                
                rd = rd << 11;
                
                binary = binary | rd;
                
                int shamt = tals.get(i).shift_amount;
                
                shamt = shamt << 6;
                
                binary = binary | shamt;
                
                int funct = 0b100001;
                
                binary = binary | funct;
                
                result.add(binary);
                binary = 0b00000000000000000000000000000000;   
        }
        if(tals.get(i).instruction_id.equals(Instruction.ID.or)){ 
                
                int rs = tals.get(i).rs;
                
                rs = rs << 21;
                
                binary = binary | rs;
                
                int rt = tals.get(i).rt;
                
                rt = rt << 16;
                
                binary = binary | rt;
                
                int rd = tals.get(i).rd;
                
                rd = rd << 11;
                
                binary = binary | rd;
                
                int shamt = tals.get(i).shift_amount;
                
                shamt = shamt << 6;
                
                binary = binary | shamt;
                
                int funct = 0b100101;
                
                binary = binary | funct;
                
                result.add(binary);
                binary = 0b00000000000000000000000000000000;   
        }
        if(tals.get(i).instruction_id.equals(Instruction.ID.slt)){ 
                
                int rs = tals.get(i).rs;
                
                rs = rs << 21;
                
                binary = binary | rs;
                
                int rt = tals.get(i).rt;
                
                rt = rt << 16;
                
                binary = binary | rt;
                
                int rd = tals.get(i).rd;
                
                rd = rd << 11;
                
                binary = binary | rd;
                
                int shamt = tals.get(i).shift_amount;
                
                shamt = shamt << 6;
                
                binary = binary | shamt;
                
                int funct = 0b101010;
                
                binary = binary | funct;
                
                result.add(binary);
                binary = 0b00000000000000000000000000000000;   
        }
        if(tals.get(i).instruction_id.equals(Instruction.ID.j)){ 
                
                binary = 0b10;
                
                binary = binary << 26;
                
                int address = tals.get(i).jump_address;
                
                binary |= address;
                
                result.add(binary);
                binary = 0b00000000000000000000000000000000;   
        }
                
        }
        return result;
    
    }
}
