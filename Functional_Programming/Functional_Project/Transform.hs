module Transform where

import Bracket
import Data.Tree
import BracketBuilding

{- This function is to change representation from a Bracket, which is structured as a tree,
   into a FlatBracket, which is just a list of FlatGames. -}  

--traverse Bracket in post-order
travGame :: Bracket -> [Bracket]
--base case round1
travGame (Game o (Competitor a) (Competitor b)) = [(Game o (Competitor a) (Competitor b))]
--recursive case/induction
travGame (Game o c d) = travGame c ++ travGame d ++ [(Game o c d)]

--helper for converting types later
whoWon :: Bracket -> Team
whoWon (Game LeftWins (Competitor (SeededTeam n0 a)) (Competitor (SeededTeam n1 b))) = a
whoWon (Game RightWins (Competitor (SeededTeam n0 a)) (Competitor (SeededTeam n1 b))) = b
whoWon (Game Unknown (Competitor (SeededTeam n0 a)) (Competitor (SeededTeam n1 b))) = "Unknown"

whoWon (Game LeftWins c d) = whoWon c
whoWon (Game RightWins c d) = whoWon d
whoWon (Game Unknown c d) = "Unknown"

--helper for converting types later
whoWon2 :: FlatGame -> (Maybe Team)
whoWon2 (FlatGame region roundName LeftWins a b) = Just a
whoWon2 (FlatGame region roundName RightWins a b) = Just b
whoWon2 (FlatGame region roundName Unknown a b) = Nothing


{-
Following helpers are round and region lists 
indicies calculated for march madness bracket traversed post-order
-}

firstReg :: Bracket -> [Bracket]
firstReg a = [((travGame a) !! 0),((travGame a) !! 1),((travGame a) !! 3),((travGame a) !! 4),((travGame a) !! 7),((travGame a) !! 8),((travGame a) !! 10), ((travGame a) !! 11)]

secondReg :: Bracket -> [Bracket]
secondReg a = [((travGame a) !! 15),((travGame a) !! 16),((travGame a) !! 18), ((travGame a) !! 19), ((travGame a) !! 22), ((travGame a) !! 23), ((travGame a) !! 25), ((travGame a) !! 26)] 

thirdReg :: Bracket -> [Bracket]
thirdReg a = [((travGame a) !! 31), ((travGame a) !! 32), ((travGame a) !! 34), ((travGame a) !! 35), ((travGame a) !! 38), ((travGame a) !! 39), ((travGame a) !! 41), ((travGame a) !! 42)] 

fourthReg :: Bracket -> [Bracket]
fourthReg a = [((travGame a) !! 46), ((travGame a) !! 47), ((travGame a) !! 49), ((travGame a) !! 50), ((travGame a) !! 53), ((travGame a) !! 54), ((travGame a) !! 56), ((travGame a) !! 57)]



round2Games1Reg :: Bracket -> [Bracket]
round2Games1Reg a = [((travGame a) !! 2), ((travGame a) !! 5), ((travGame a) !! 9), ((travGame a) !! 12)]

round2Games2Reg :: Bracket -> [Bracket]
round2Games2Reg a = [((travGame a) !! 17), ((travGame a) !! 20), ((travGame a) !! 24), ((travGame a) !! 27)]

round2Games3Reg :: Bracket -> [Bracket]
round2Games3Reg a = [((travGame a) !! 33), ((travGame a) !! 36), ((travGame a) !! 40), ((travGame a) !! 43)]

round2Games4Reg :: Bracket -> [Bracket]
round2Games4Reg a = [((travGame a) !! 48), ((travGame a) !! 51), ((travGame a) !! 55), ((travGame a) !! 58)]



round3Games1Reg :: Bracket -> [Bracket]
round3Games1Reg a = [((travGame a) !! 6), ((travGame a) !! 13)]

round3Games2Reg :: Bracket -> [Bracket]
round3Games2Reg a = [((travGame a) !! 21), ((travGame a) !! 28)] 

round3Games3Reg :: Bracket -> [Bracket]
round3Games3Reg a = [((travGame a) !! 37), ((travGame a) !! 44)] 

round3Games4Reg :: Bracket -> [Bracket]
round3Games4Reg a = [((travGame a) !! 52), ((travGame a) !! 59)]

round4Games1Reg:: Bracket -> [Bracket]
round4Games1Reg a = [((travGame a) !! 14)] 

round4Games2Reg:: Bracket -> [Bracket]
round4Games2Reg a = [((travGame a) !! 29)] 

round4Games3Reg :: Bracket -> [Bracket]
round4Games3Reg a = [((travGame a) !! 45)] 

round4Games4Reg :: Bracket -> [Bracket]
round4Games4Reg a = [((travGame a) !! 60)]

round5Game1Reg :: Bracket -> [Bracket]
round5Game1Reg a = [((travGame a) !! 30)] 

round5Game2Reg :: Bracket -> [Bracket]
round5Game2Reg a = [((travGame a) !! 61)]

finalGame :: Bracket -> [Bracket]
finalGame a = [((travGame a) !! 62)]

--genFlatGames and genFlatGames2 use above region and round helpers to gen appropriate lists of FlatGames
genFlatGames :: [Bracket] -> Region -> RoundName -> [FlatGame]
genFlatGames [] _ _ = []
genFlatGames ((Game o (Competitor (SeededTeam seed1 team1)) (Competitor (SeededTeam seed2 team2))):xs) region roundName = [(FlatGame region roundName o team1 team2)] ++ genFlatGames xs region roundName

genFlatGames2 :: [Bracket] -> Region -> RoundName -> [FlatGame]
genFlatGames2 [] _ _ = []
genFlatGames2 ((Game o (Game o2 b1 b2) (Game o3 b3 b4)):xs) region roundName = [(FlatGame region roundName o (whoWon (Game o2 b1 b2)) (whoWon (Game o3 b3 b4)))] ++ genFlatGames2 xs region roundName

flattenBracket :: Bracket -> FlatBracket
flattenBracket a = (FlatBracket (genFlatGames (firstReg a) East Round1 ++ genFlatGames (secondReg a) Midwest Round1 ++ genFlatGames (thirdReg a) South Round1 ++ genFlatGames (fourthReg a) West Round1 ++ genFlatGames2 (round2Games1Reg a) East Round2 ++ genFlatGames2 (round2Games2Reg a) Midwest Round2 ++ genFlatGames2 (round2Games3Reg a) South Round2 ++ genFlatGames2 (round2Games4Reg a) West Round2 ++ genFlatGames2 (round3Games1Reg a) East RegionalSemis ++ genFlatGames2 (round3Games2Reg a) Midwest RegionalSemis ++ genFlatGames2 (round3Games3Reg a) South RegionalSemis ++ genFlatGames2 (round3Games4Reg a) West RegionalSemis ++ genFlatGames2 (round4Games1Reg a) East RegionalFinals ++ genFlatGames2 (round4Games2Reg a) Midwest RegionalFinals ++ genFlatGames2 (round4Games3Reg a) South RegionalFinals ++ genFlatGames2 (round4Games4Reg a) West RegionalFinals ++ genFlatGames2 (round5Game1Reg a) East NationalSemis ++ genFlatGames2 (round5Game2Reg a) South NationalSemis ++ genFlatGames2 (finalGame a) East NationalChampionship))


{- build a binary tree where each node is labeled by the team the Bracket
   said won that game, or Nothing if the Bracket labeled that game as Unknown -}

makeMaybeList :: FlatBracket -> [(Maybe Team)]
makeMaybeList (FlatBracket(x:xs)) = (whoWon2 x: makeMaybeList (FlatBracket xs))

-- first int is index second is round makes uses of the fact that the Tree is bin to find child nodes
b2TreeH :: [(Maybe Team)] -> Int -> Int -> Tree (Maybe Team)
b2TreeH aList i 5 = (Node (aList !! i) [])
b2TreeH aList i r = (Node (aList !! i) [ b2TreeH aList (2*i+1) (r+1), b2TreeH aList (2*i+2) (r+1)])

--flatten the bracket convert the types reverse the order and pass into helper to finish
bracketToTree :: Bracket -> Tree (Maybe Team)
bracketToTree a = b2TreeH (reverse(makeMaybeList(flattenBracket a))) 0 0