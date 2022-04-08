-- function for scoring brackets
module Scoring where

import Bracket

import Transform

import Data.Tree

{- a ScoringScheme is a list of points to give for correct answers for each round, ordered from round1 through the
   championship.  -}
type ScoringScheme = [Int]

-- Apparently (from NYTimes) this is the standard scoring scheme
standardScheme = [1,2,4,8,16,32]

-- another popular scheme
stepScheme = [1,2,3,4,5,6]

{- the first bracket gives the outcomes of the games against which to score the second bracket.
   If the second bracket has a different outcome for a game than the first, or if either lists
   the outcome as Unknown, then the second bracket does not get any points for that game.  Otherwise
   it gets the points for the current round given by the score scheme. -}

--need to iterate through the brackets

--need a counter for the rounds

--keep count of right answers

--output the score
scoreBracketH :: Eq a => ScoringScheme -> [[a]] -> [[a]] -> Int-> Int -> Int -> Int
scoreBracketH (x:xs) ansList testList round winnerInRoundIndex score = 

    
    if ((ansList !! round) !! winnerInRoundIndex) == ((testList !! round) !! winnerInRoundIndex) && length(testList) /= (winnerInRoundIndex + 1)  then scoreBracketH (x:xs) ansList testList round (winnerInRoundIndex + 1) (x + score) else
    if ((ansList !! round) !! winnerInRoundIndex) == ((testList !! round) !! winnerInRoundIndex) && length(testList) == (winnerInRoundIndex + 1)  then scoreBracketH xs (tail(ansList)) (tail(testList)) (round + 1) 0 (x + score) else
    if ((ansList !! round) !! winnerInRoundIndex) /= ((testList !! round) !! winnerInRoundIndex) && length(testList) /= (winnerInRoundIndex + 1)  then scoreBracketH (x:xs) ansList testList round (winnerInRoundIndex + 1) (score) else
    if ((ansList !! round) !! winnerInRoundIndex) /= ((testList !! round) !! winnerInRoundIndex) && length(testList) == (winnerInRoundIndex + 1)  then scoreBracketH xs (tail(ansList)) (tail(testList)) (round + 1) 0 (score) else
    score

scoreBracketH _ [] _ _ _ score = score

scoreBracketH _ _ [] _ _ score = score


-- change Bracket to Tree to lists of list in reverse order to align with ScoringScheme
scoreBracket :: ScoringScheme -> Bracket -> Bracket -> Int
scoreBracket (x:xs) answerBracket testBracket = scoreBracketH (x:xs) (reverse(levels(bracketToTree(answerBracket)))) (reverse(levels(bracketToTree(testBracket)))) 1 0 0