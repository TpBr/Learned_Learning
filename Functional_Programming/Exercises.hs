module Exercises where

import Data.List

----------------------------------------------------------------------
-- Recursing through lists
--
-- The following problems may be solved by writing recursive
-- functions which pattern match on an input list (or lists).
--
-- We will do more examples in class, but you can find one already 
-- in lec/jan28-maybe--pattern-matching/Inclass.hs,
-- namely anyNothingList.
----------------------------------------------------------------------

{- drop every other element from the input list, beginning
   with the first element.  So p1 [1,2,3,4,5,6] should return
   [2,4,6]. For a one-element list, just return the empty list. -}
p1 :: [a] -> [a]
p1 xs  = [x | (x, i) <- zip xs [0..length xs - 1], (rem i 2) /= 0]

{- drop every other element from the input list, beginning
   with the second element.  So p1 [1,2,3,4,5,6] should return
   [1,3,5]. -}
p2 :: [a] -> [a]
p2 xs  = [x | (x, i) <- zip xs [0..length xs - 1], (rem i 2) == 0] 

{- duplicate every element in the list.  So p3 "abc" should return
   "aabbcc". -}
p3 :: [a] -> [a]
p3 x = concat ( map (replicate 2) x )

{- tower of exponents: [1,2,3,4] should turn into 1 ^ 2 ^ 3 ^ 4
   [] can just turn into 1, as a corner case (and also this is
   helpful for defining the function recursively.) -}
p4 :: Integral a => [a] -> a
p4 x = foldr (^) 1 x
  
{- This function is supposed to create a new list consisting of
   alternating elements of the two input lists (so first from
   the first list, then from the second, then from the first
   again, etc.). So p1 [1,3,5] [2,4,6] should produce [1,2,3,4,5,6].
   When the list to choose elements from runs out, you just give
   all the elements of the other list.  This handles the case
   where the lists are not the same length. -}
p5 :: [a] -> [a] -> [a]
p5 [] ys = ys
p5 xs [] = xs
p5 xs ys = (head(xs)):(head(ys)):p5 (tail(xs)) (tail(ys))

----------------------------------------------------------------------
-- Operations on trees
--
-- These problems are to help get you used to programming with
-- user-declared datatypes.  Some of these require recursion, while
-- others do not.
----------------------------------------------------------------------

-- here is a datatype for binary trees with data at the nodes
data Tree a = Leaf | Node a (Tree a) (Tree a) deriving (Show , Eq)

-- inject a piece of data as a Node whose left and right subtrees
-- are leaves.  So p6 3 should return Node 3 Leaf Leaf.
p6 :: a -> Tree a
p6 a  = Node a Leaf Leaf 

-- count the number of elements (i.e., the number of uses of Node)
p7 :: Tree a -> Int
p7 Leaf = 0
p7 (Node a leftTree rightTree) = 1 + (p7 leftTree) + (p7 rightTree) 

{- given an element and a tree, build a new tree with that
   element at the root and the tree as both the left and right
   subtree.  So p8 3 (Node 1 Leaf Leaf) would return
   Node 3 (Node 1 Leaf Leaf) (Node 1 Leaf Leaf). -}
p8 :: a -> Tree a -> Tree a
p8 a tree  = (Node a tree tree) 

{- return the elements of the tree using an in-order traversal.  This
   means that for any Node, you should list the elements of the left
   subtree, then the data at that Node, and then the elements of the
   right subtree.

   See, for example,
   https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/ -}
p9 :: Tree a -> [a]
p9 Leaf = []
p9 (Node a leftTree rightTree) = (p9 leftTree) ++ [a] ++ (p9 rightTree) 

-- do the same thing as for p9, but use a post-order traveral. 
p10 :: Tree a -> [a]
p10 Leaf = []
p10 (Node a leftTree rightTree) = (p10 leftTree) ++ (p10 rightTree) ++ [a]

{- apply the given function to all the data in the input tree,
   constructing a new tree with the same structure (but holding
   the outputs of the function). -}
p11 :: (a -> b) -> Tree a -> Tree b
p11 f Leaf = Leaf
p11 f (Node a leftTree rightTree) = (Node (f a) (p11 f leftTree) (p11 f rightTree))

-- recursively flip left and right subtrees throughout the tree
p12 :: Tree a -> Tree a
p12 (Node a Leaf rightTree) = (Node a rightTree Leaf)
p12 (Node a leftTree Leaf) = (Node a Leaf leftTree)
p12 (Node a leftTree rightTree) = (Node a (p12 rightTree) (p12 leftTree))

-- return the root of the tree if it has one
p13 :: Tree a -> Maybe a
p13 Leaf = Nothing
p13 (Node a leftTree rightTree) = Just a

{---------------------------------------------------------------------
 A more complex datatype

 The following code is taken from
 http://book.realworldhaskell.org/read/writing-a-library-working-with-json-data.html

 JSON is a textual format commonly used for exchanging structured data between
 clients and servers in web applications.  There are just a few forms of data
 allowed.  

 A tiny explanation is given below with p14.

 See various online references for a tutorial if needed, like
     https://www.w3schools.com/js/js_json_intro.asp
----------------------------------------------------------------------}

-- elements of the JValue datatype represent JSON text
data JValue = JString String
            | JNumber Double
            | JBool Bool
            | JNull
            | JObject [(String, JValue)]
            | JArray [JValue]
              deriving (Eq, Ord)

{- this function turns a JValue into a syntactically correct JSON string (except
   that it does not implement JSON rules for escape sequences like \n, but this
   is not important for the problems below). -}
renderJValue :: JValue -> String
renderJValue (JString s)   = show s
renderJValue (JNumber n)   = show n
renderJValue (JBool True)  = "true"
renderJValue (JBool False) = "false"
renderJValue JNull         = "null"
renderJValue (JObject o) = "{" ++ pairs o ++ "}"
  where pairs [] = ""
        pairs ps = intercalate ", " (map renderPair ps)
        renderPair (k,v)   = show k ++ ": " ++ renderJValue v
renderJValue (JArray a) = "[" ++ values a ++ "]"
  where values [] = ""
        values vs = intercalate ", " (map renderJValue vs)

instance Show JValue where
  show = renderJValue

{- Implement the JSON value

     { "id" : 51 ,
       "public" : false ,
       "JobPairs" : [ { "id" : 31 , "solverid" : 1 , "benchid" : 251 } ,
                      { "id" : 32 , "solverid" : 1 , "benchid" : 58  } ,
                      { "id" : 33 , "solverid" : 2 , "benchid" : 251  } ] }

   as a value of type JValue.  (This could represent some information from
   starexec.org, if you are curious -- but the semantics of this sample
   JSON text is not important.)

   Square brackets are for arrays, curly brackets are for objects.

   I found it handy to write a helper function for creating the JSON for
   a job pair like { "id" : 33 , "sid" : 2 , "bid" : 251  }.
   Then I can call this helper function three times, rather than write out
   three rather bulky JValue expressions directly.
   -}
toInt = (\x -> JNumber (fromInteger x))
p14 :: JValue
p14 = JObject [pair("id", 51) toInt, pair ("public", False) (\x -> JBool x), pair ("JobPairs", JArray [JObject [pair ("id", 31) toInt, pair ("sid", 1) toInt, pair ("bid", 251) toInt], JObject [pair ("id", 32) toInt, pair ("sid", 1) toInt, pair ("bid", 58) toInt], JObject [pair ("id", 33) toInt, pair ("sid", 2) toInt, pair ("bid", 251) toInt]]) (\x -> x) ]   

--Helper function for pairs as suggested
pair :: (a,b) -> (b -> c) -> (a, c)
pair a f = (fst a, f (snd a))

-- return True if the input JValue is JNull, and False otherwise
p15 :: JValue -> Bool
p15 a = if a == JNull then True else False

{- return the list of attribute-value pairs if the input JValue is a JObject. -}   
p16 :: JValue -> Maybe [(String , JValue)]
p16 (JObject a)  = Just a
p16 _ = Nothing

{- replace JString "null" everywhere you find it with JNull (do not try to
   replace attributes of JObjects like in { "null" : 3 }) -}
p17 :: JValue -> JValue
p17 (JString "null") = JNull
p17 (JArray (a:as)) = JArray (p17H (a:as)) 
p17 (JObject (x:xs)) = JObject (p17Object (x:xs))

--Recurse through a list from a JArray looking for JString "null"
p17H ::  [JValue] -> [JValue]
p17H [] = []
p17H (x:xs) = ((p17HH x) : (p17H xs))

--switch if necessary
p17HH :: JValue -> JValue
p17HH (JString "null") = JNull
p17HH (JObject (x:xs)) = p17 (JObject (x:xs))
p17HH a = a

--helper for handling data inside JObjects
p17Object :: [(String, JValue)] -> [(String, JValue)]
p17Object [] = []
p17Object (x:xs) = ( (pTupleHelper x): (p17Object xs) )

--need helper to look at tuples inside list inside
pTupleHelper :: (String, JValue) -> (String, JValue)
pTupleHelper (a, b)  = (a, (p17HH b)) 

{- return a list of all the values v for which the attribute-value pair (s,v)
   occurs in the JValue, where s is the given input String. -}
p18 :: String -> JValue -> [JValue]
p18 _  JNull  = []
p18 _  (JString x) = []
p18 _ (JNumber x) = []
p18 _ (JBool x) = []
p18 stringInput  (JObject (x:xs)) = (p18Helper0 stringInput (x:xs) )
p18 stringInput (JArray (x:xs)) = (p18 stringInput x) ++  (p18 stringInput (JArray xs))
p18 a b = []

--Helper for recursing through data inside JObject
p18Helper0 :: String -> [(String, JValue)] -> [JValue]
p18Helper0 stringInput [] = []
p18Helper0 stringInput (x:xs) = ((p18Helper1 stringInput x): ( p18Helper0 stringInput xs))

--Similar to above helper but needed to return JValue instead of [JValue] in cases of nested JObjects for example
p18Helper0b :: String -> [(String, JValue)] -> JValue
p18Helper0b stringInput [] = JNull
p18Helper0b stringInput (x:xs) = (p18Helper1 stringInput x)

--helper that does the actual specified checking
p18Helper1 :: String -> (String, JValue) -> JValue
p18Helper1 stringInput (a, (JObject b) ) = if stringInput == a then (JObject b) else (p18Helper0b stringInput b)
p18Helper1 stringInput (a, b) = if stringInput == a then b else JNull
