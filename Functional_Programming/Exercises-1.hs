module Exercises where

import E
import Data.List

{- given an input list of tuples of the form ((x,y),n),
   return the list of those values n where x == y.

   Hint: try some combination of map and filter. -}

tupleIsEqual ((a,b), c)  = if a == b then True else False
       
p1 :: Eq a => [((a,a),b)] -> [b]
p1 x  = map snd (filter tupleIsEqual x)

{- p2 n ns should subtract the numbers in ns from n.
   So p2 10 [1,2,3] equals ((10 - 1) - 2) - 3.

   Hint: try a foldl. -}
p2 :: Int -> [Int] -> Int
p2 a x = foldl (-) a x

{- compose corresponding functions from the two lists,
   creating a list of the resulting compositions.  If one
   list is longer, drop the excess.

   Hint: use zipWith -}
p3 :: [b -> c] -> [a -> b] -> [a -> c]
p3 f g  = zipWith (.) f g 

{- change the order of the types in the input tuple of a function.  This is
   like the flip function we saw in class (or run ':type flip' in the REPL),
   except for uncurried functions. -}
p4 :: ((a,b) -> c) -> (b,a) -> c
p4 f (a,b) = f (b, a)

{- create a list of all the suffixes of the input list.  So
   p5 "abc" should returned ["abc","bc","c",""].  The order of the
   suffixes in the list does not matter. -}
p5 :: [a] -> [[a]]
p5 [] = []
p5 x = if length x == 1 then x: [[]] else x: p5 ( tail x )

e1 :: Int -> Int
e1 a = 3 - a

e2 :: Int -> [Int] -> [Int]
e2 a b = map (+ a) b 

e3 :: (Int,Int) -> (Int,Int)
e3 (a,b) = mapPair (3 + ) (3 -  ) (a,b) 

 --Just uncomment the ones you choose to implement:

--r1 :: Eq a => E ([((a,a),b)] -> [b])
--r1 = undefined

r2 :: E (Int -> [Int] -> Int)
r2 = Foldl :@ Subtract

r3 :: E ([b -> c] -> [a -> b] -> [a -> c])
r3 = ZipWith :@ Compose

r4 :: E (  ((a,b) -> c) -> (b,a) -> c )
r4 = Compose :@ (Compose :@ Uncurry :@ Flip) :@ Curry

--r5 :: E ([a] -> [[a]])
--r5 = undefined 
