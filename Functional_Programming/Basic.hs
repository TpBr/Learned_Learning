module Basic where

import Data.Ratio
import Data.Maybe
import Data.List

hello :: String
hello = "Welcome to Haskell!"

----------------------------------------------------
-- Tuples
----------------------------------------------------

missing :: Monad m => m a
missing = fail "need to implement"

-- add the components of the input tuple
p1 :: (Int,Int,Int) -> Int
p1 = \(x,y,z) -> x + y + z

-- swap the components of the input tuple
p2 :: (a, b) -> (b, a)
p2 = \(x, y) -> (y, x)

-- add the two input tuples as vectors (so add first components, then add second components)
p3 :: (Int,Int) -> (Int,Int) -> (Int,Int)
p3 = \(a, b) -> (\(x, y) -> (a + x, b + y))

-- combine two pairs into a tuple with four components
p4 :: (a,b) -> (c,d) -> (a,b,c,d)
p4 = \(q, w) -> (\(e, r) -> (q, w, e, r))

-- apply a function to each component of a tuple, building a new tuple
p5 :: (a -> b) -> (a,a) -> (b,b)
p5  = \(f) -> (\(a, b) -> (f a, f b))

----------------------------------------------------
-- Strings and converting to strings
----------------------------------------------------

-- duplicate the input string (so return a string with two copies of s back to back)
p6 :: String -> String
p6 = \a -> a ++ a

-- reverse the input string
p7 :: String -> String
p7 = \a -> reverse a

-- Concatenate the strings with " is " in the middle.
-- So p8 "the dog" "lazy" should return "the dog is lazy"
p8 :: String -> String -> String
p8 = \a -> (\b -> (a ++ " is " ++ b))

{- print the rational number the default way, which is numerator % denominator.

   HINT: read the docs on Rational, here
   http://hackage.haskell.org/package/base-4.12.0.0/docs/Data-Ratio.html
-}
p9 :: Rational -> String
p9 = \a -> (show (numerator a) ++ " % " ++ show (denominator a))

-- print the rational number as numerator / denominator
p10 :: Rational -> String
p10 = \a -> (show (numerator a) ++ " / " ++ show (denominator a))

----------------------------------------------------
-- Functions
----------------------------------------------------

-- p11 f x should call f with x and x as f's two inputs
-- reminds me of the omego combinator if my code's correct
p11 :: (a -> a -> c) -> a -> c
p11 = \f -> (\x -> f x x)

{- take in
   f :: a -> b -> c
   g :: a -> b
   h :: a

   and produce a value of type c (so you need to call f and
   g each with input h as part of this) -}
p12 :: (a -> b -> c) -> (a -> b) -> a -> c
p12 = \f -> (\g -> (\h -> (f h) (g h)))

{- there is actually only one nonfailing nondiverging function you can write
   that has this type! -}
p13 :: (b,c) -> (b -> c) -> ((c,c) -> d) -> d
p13 = \(x,y) -> (\f -> (\g -> g (f x, y)))

----------------------------------------------------
-- Maybe type
----------------------------------------------------

{- p14 x y z: if x is Nothing return y,
   otherwise if x is Just v return z v -}
p14 :: Maybe a -> b -> (a -> b) -> b
p14 = \x -> (\y -> (\z -> maybe y z x))

{- if the first input is nothing, return the second;
   otherwise return the first input -}
--was unable to use maybe type as the if itself 
--used condition w/ isJust instead
p15 :: Maybe a -> Maybe a -> Maybe a
p15  = \x -> (\y ->  if isJust x then x else y)

----------------------------------------------------
-- Lists
--
-- Hint: read the docs on Data.List
----------------------------------------------------

-- return the number of non-zero values in the input list
p16 :: [Int] -> Int
p16 = \xs -> length [x| x <- xs, x > 0]

-- return a new list which is the concatenation of the three inputs lists
p17 :: [a] -> [a] -> [a] -> [a]
p17 = \a -> (\b -> (\c -> a ++ b ++ c))

-- return a list which is just like the input list except without
-- the first and last elements (it can fail if the list has fewer
-- than 2 elements
p18 :: [a] -> [a]
p18 = \x -> init((tail x))

{- given f , p , and xs, return the list of those elements x of xs
   for which f x satisfies the given predicate p -}
p19 :: (a -> b) -> (b -> Bool) -> [a] -> [a]
p19 = \f -> (\p -> (\xs -> [x| x <- xs, p (f x)]))

{- given a function and a list of inputs, construct the list of input-output pairs
   for that function on those inputs -}
p20 :: (a -> b) -> [a] -> [(a,b)]
p20 = \f -> (\xs -> [(x, (f x))| x <- xs])
