package edu.uiowa.cs;

import java.util.*;

public class Phase2 {

    /* Returns a list of copies of the Instructions with the
     * immediate field (i-type) or jump_address (j-type) of the instruction filled in
     * with the address calculated from the branch_label.
     *
     * The instruction should not be changed if it is not a branch or jump instruction.
     *
     * unresolved: input program, whose branch/jump instructions don't have resolved immediate/jump_address
     * first_pc: address where the first instruction of the program will eventually be placed in memory
     */
    public static List<Instruction> resolve_addresses(List<Instruction> unresolved, int first_pc) {
        List<Instruction> resolved = new LinkedList<>();
        Map<String, Integer> dictionary = new HashMap<String, Integer>();
        
        int counter = 0;
        int counter2 = 0;
        
        for (int j = 0; j < unresolved.size(); j++){
            
            if (!(unresolved.get(j).label.length() == 0)){
                dictionary.put(unresolved.get(j).label, j);
            }
        }
        
        for (int i = 0; i < unresolved.size(); i++){
            counter -=1;
            
            if (unresolved.get(i).instruction_id == Instruction.ID.bne){
                Instruction instruction = InstructionFactory.CreateBne(unresolved.get(i).rs, unresolved.get(i).rt, counter + dictionary.get(unresolved.get(i).branch_label), unresolved.get(i).label);
                resolved.add(instruction);
            }
            
            else if (unresolved.get(i).instruction_id == Instruction.ID.beq){
                Instruction instruction = InstructionFactory.CreateBeq(unresolved.get(i).rs, unresolved.get(i).rt, counter + dictionary.get(unresolved.get(i).branch_label), unresolved.get(i).label);
                resolved.add(instruction);
            }
            
            else if (unresolved.get(i).instruction_id == Instruction.ID.j){
                
                int temp = first_pc /4;
                int step = 4 * dictionary.get(unresolved.get(i).branch_label);
                temp += step;

                Instruction instruction = InstructionFactory.CreateJ(temp, unresolved.get(i).label);
                resolved.add(instruction);
                
                
            }
            
            else {
                resolved.add(unresolved.get(i));
            }
        }
        
        return resolved;
    }

}