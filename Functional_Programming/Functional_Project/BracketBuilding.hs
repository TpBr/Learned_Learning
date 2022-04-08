-- functions to assemble brackets
module BracketBuilding where

import Bracket

import System.IO
import Data.List
import Data.List.Split
import Data.Char

{- process the ranklist in the file whose name is given as the input to the
   function.  See ranklist2019.txt for the 2019 ranklist.  This is the format
   your code should expect.  Your job is to extract just the team names from
   those lines.
   Hint: functions in Data.List and maybe also Data.List.Split could help
   extract the team-name from each line of the file (dropping the other information) -}

--helper flags whitespace teams that need to be dropped from list
helpDropBoo :: String -> Bool
helpDropBoo x = all isSpace x

--helper uses above to actually not include all whitespace teams in list
dropEmptyStrs :: [String] -> [String]
dropEmptyStrs [s] = if (not (helpDropBoo s)) then [s] else []
dropEmptyStrs (x:xs) = if (not (helpDropBoo x)) then (x:dropEmptyStrs xs) else (dropEmptyStrs xs) 

--filters out unneeded info, leaving ')' for splitting on
filterNum :: String -> String
filterNum xs = filter ( `notElem` ['(', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '0', '.', '"', '\n']) xs 

--cuts out trailing space from string on both ends
trim :: String -> String
trim s = reverse(dropWhile isSpace (reverse(dropWhile isSpace s)))

iter :: [String] -> [String]
iter aList = map trim aList

--putting above text cleanin helpers together to mine txt
readRankList :: String -> IO [Team]
readRankList teamFile =
   do 
   contents <- readFile teamFile

   let contents1 = filterNum contents

   let teamList0 = splitOn ")" contents1

   let teamList1 = iter (dropEmptyStrs teamList0)

   return teamList1

{- given a rank list (as obtained from readRankList), in order from highest-ranked
   to lowest-ranked team, construct the lists of seeded teams for the four regions.
   You should follow the following strategy (described on the Wikipedia page for
   the tournament), for which you will probably find it useful to write a helper
   function:
   The top four teams in the rank list become the number 1 seeds in the four
   regions (let us say that they are placed in the regions in the order
   below, which is alphabetical by region name).  Then the next four teams become
   the number 2 seeds in the four regions, and so on.  (We ignore all other
   considerations about determining seeds discussed on the Wikipedia page.)
-}

--grabs every four from a list of Teams for a region (since txt in ranked order)
regionSeparate :: [Team] -> Int -> [SeededTeam]
regionSeparate (a:b:c:d:xs) n = ((SeededTeam n a): regionSeparate xs (n+1))
regionSeparate [x, y, z] n = [(SeededTeam n x)]
regionSeparate [x, y] n = [(SeededTeam n x)]
regionSeparate [x] n = [(SeededTeam n x)]
regionSeparate _ n = []

--calls above to generate 4-tuple of lists of Seeded Teams (one for each region)
buildRegions :: [Team] -> ([SeededTeam],[SeededTeam],[SeededTeam],[SeededTeam])
buildRegions (a:b:c:xs) = (regionSeparate (a:b:c:xs) 1, regionSeparate (b:c:xs) 1, regionSeparate (c:xs) 1,regionSeparate xs 1)

{- use buildRegions to create the initial Competitors, and then
   combine them into a single Bracket, where all Outcomes should be Unknown.
   The resulting Bracket should satisfy the requirement that a team with seed n
   is paired in the first round of the bracket with a team of seed 17-n (so the 1-seed
   is paired with the 16-seed in the region, the 2-seed with the 15-seed, and so forth).
-}

--helper that takes a SeededTeam and creates base case bracket (competitor)
makeComp :: [SeededTeam] -> [Bracket]
makeComp [a] = [Competitor a]
makeComp (x:xs) = ((Competitor x):(makeComp xs))
makeComp _ = []

--combines brackets in regions into games with correct seeds against eachother
makeTree :: [Bracket] -> Int -> Int -> Bracket
makeTree aList 7 8 = (Game Unknown (aList !! 7) (aList !! 8))
makeTree aList n m = (Game Unknown (makeTree aList (n+1) (m-1)) (Game Unknown (aList !! n) (aList !! m)))

--tuple select helpers for picking out regions
select1 :: (x, x, x, x) -> x
select1 (a, b, c, d) = a

select2 :: (x, x, x, x) -> x
select2 (a, b, c, d) = b

select3 :: (x, x, x, x) -> x
select3 (a, b, c, d) = c

select4 :: (x, x, x, x) -> x
select4 (a, b, c, d) = d

--calls everything together to gen one bracket
buildBracket :: [Team] -> Bracket
buildBracket aList = (Game Unknown (Game Unknown (makeTree (makeComp (select1 (buildRegions aList ))) 0 15) (makeTree (makeComp (select2 (buildRegions aList ))) 0 15) ) (Game Unknown (makeTree (makeComp (select3 (buildRegions aList ))) 0 15) (makeTree (makeComp (select4 (buildRegions aList ))) 0 15) ))

{- combine above functions to go from the name of a file containing a ranklist
   to a Bracket. -}
bracketFromFile :: String -> IO Bracket
bracketFromFile teamFile1 = do 
   let teams = readRankList teamFile1
   ts <- teams
   let ans = buildBracket ts
   
   return ans