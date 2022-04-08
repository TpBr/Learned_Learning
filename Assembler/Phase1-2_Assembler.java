package edu.uiowa.cs;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class Phase1 {

    /* Translates the MAL instruction to 1-3 TAL instructions
     * and returns the TAL instructions in a list
     *
     * mals: input program as a list of Instruction objects
     *
     * returns a list of TAL instructions (should be same size or longer than input list)
     */
    public static List<Instruction> mal_to_tal(List<Instruction> mals) {
        List<Instruction> tals = new LinkedList<>();
        for (int i = 0; i < mals.size(); i++){
            if (mals.get(i).instruction_id.equals(Instruction.ID.blt)){
                
                Instruction temp1 = InstructionFactory.CreateSlt(1, mals.get(i).rt, mals.get(i).rs);
                Instruction temp2 = InstructionFactory.CreateBne(1, 0,  mals.get(i).branch_label, mals.get(i).label);
                
                tals.add(temp1);
                tals.add(temp2);
            }
            
            else if (mals.get(i).instruction_id.equals(Instruction.ID.bge)){
                
                Instruction temp3 = InstructionFactory.CreateSlt(1, mals.get(i).rt, mals.get(i).rs);
                Instruction temp4 = InstructionFactory.CreateBeq(1, 0, mals.get(i).branch_label, mals.get(i).label);
                
                tals.add(temp3);
                tals.add(temp4);
            }
            
            else if ((mals.get(i).instruction_id.equals(Instruction.ID.addiu) && (mals.get(i).immediate > (0xFFFF)))){
                
               int upper = mals.get(i).immediate >>> 16;
               int lower = mals.get(i).immediate & 0x0000FFFF;
               
               Instruction temp5 = InstructionFactory.CreateLui(1, upper, mals.get(i).label);
               Instruction temp6 = InstructionFactory.CreateOri(1, 1, lower);
               Instruction temp7 = InstructionFactory.CreateAddu(mals.get(i).rt, mals.get(i).rs, 1);
               
               tals.add(temp5);
               tals.add(temp6);
               tals.add(temp7);
            }
        
            else if (mals.get(i).instruction_id.equals(Instruction.ID.ori) && (mals.get(i).immediate > (0xFFFF))){
                
               int upper = mals.get(i).immediate >>> 16;
               int lower = mals.get(i).immediate & 0x0000FFFF;
               
               Instruction temp8 = InstructionFactory.CreateLui(1, upper, mals.get(i).label);
               Instruction temp9 = InstructionFactory.CreateOri(1, 1, lower);
               Instruction temp10 = InstructionFactory.CreateOr(mals.get(i).rt, mals.get(i).rs, 1);
               
               tals.add(temp8);
               tals.add(temp9);
               tals.add(temp10);
            }
            else {
                
                Instruction t = mals.get(i).copy();
                tals.add(t);
            }
        }
        return tals;
    }
}