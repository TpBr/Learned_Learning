module sortedLists where

open import lib

{- we use internal verification to define a datatype of sorted lists
   of natural numbers, where typing ensures that the lists are truly
   sorted in non-decreasing order.

   A list of type (sortedList n) is sorted and guaranteed to have 
   all its data greater than or equal to n; so n is a lower bound
   on the data in the list.  Keeping this lower bound explicit in
   the type enables us to require a proof of a constant-time check,
   namely d ≤ n, when insert d into a list with lower-bound n.  For
   cons nodes, we allow the lower-bound to be less than the head of
   the list.  This is needed for merge below.

   There are three constructors:

   -- nil, as usual (empty list)
   -- cons, as usual (build a new list from head and tail)
   -- weaken, decrease the lower bound (this was missing in my first
      attempt, which led to nasty problems in the case of merge below)

 -}

data sortedList : ℕ → Set where
  nil : ∀ (n : ℕ) → sortedList n  -- empty lists can have any lower bound you like
  cons : ∀ (d : ℕ) → -- the head of the list
           {n : ℕ} → -- the lower-bound for the tail
           sortedList n → -- the tail of the list, with lower bound n on its data
           d ≤ n ≡ tt → {- proof that d is less than or equal to that lower bound, and
                           hence less than or equal to all data in the tail -}
           sortedList d -- d is the lower bound for the new list created by the cons
  weaken : ∀ (n : ℕ) {n' : ℕ} → sortedList n' → n ≤ n' ≡ tt → sortedList n

-- fill in the holes below, just to help you get a feel for how the sortedList datatype works
-- [5 points]
simple : sortedList 1
simple = weaken 1 (cons 2 (nil 3) refl) refl

{- glb stands for greatest lower bound.  min' d n is the greatest 
   lower bound of d and n, in the sense that if any other d' is a lower bound 
   of both d and n, then it is also a lower bound of min' d n.  (Ideas from 
   basic lattice theory.) 

   To prove this, you will run into a mess if you case split on d', d, or n.
   Instead, you should consider cases for whether or not d ≤ n.  You can use
   "with" for this, as discussed in Section 4.3.3 (page 86) of the book. 
   -}
-- [10 points]


glb : ∀ d' d n → d' ≤ d ≡ tt → d' ≤ n ≡ tt → d' ≤ min d n ≡ tt
glb d' d n p p'  with d < n
glb d' d n p p' | tt  = p
glb d' d n p p'  | ff = p'

{- insert d xs should insert d into xs as the right position to keep the list
   sorted.  

   So you will case split on xs (the sortedList), and in the cons case, 
   consider whether the data you are inserting is ≤ the data at the head of the
   list.

   I found I needed to use the "with keep" idiom; see Section 4.3.3 (page 90).

   Another hint: I also needed a few theorems from nat-thms.agda in the IAL: 

     <≤, min-mono2, <ff

  Note that you can pattern match on implicit arguments, for example for a cons, like this:

  (cons d' {n} xs x)

  The {n} is used to match on that implicit lower-bound for the sortedList xs.

  [15 points]
-}

lemm0 : ∀ (d  d1  n : ℕ) → d < d1 ≡ ff → d1 ≤ n ≡ tt → d1 ≤ min d n ≡ tt
lemm0 d d1 n b x with keep (d < n)
lemm0 d d1 n b x | tt , e rewrite e =  (<ff {d} {d1} b)
lemm0 d d1 n b x | ff , e rewrite e = x


insert : ∀ (d : ℕ) → {n : ℕ} → sortedList n → sortedList (min d n)
insert d (nil n) with keep(d <  n  )

insert d (nil n) | tt , p rewrite p = weaken d (cons d (nil n) (<≤ {d} {n} p)) (≤-refl d)
insert d (nil n) | ff , p rewrite p = (cons n (nil d) (<ff {d} {n}  p))

insert d (cons d1 {n} xs x) with keep ( d < d1 )
insert zero (cons zero {zero} xs x) | tt , b rewrite b = (cons zero (cons zero xs x) x)
insert d (cons d1 {suc t} xs x) | tt , b rewrite b = weaken d (cons d ( cons d1 xs x)  (<≤ {d} {d1} b)) (≤-refl d) 
insert d (cons d1 {n} xs x) | ff , b rewrite b   = (cons d1 ( insert d xs)  (lemm0 d d1 n b x) )

insert d (weaken n xs x) with keep ( d < n)
insert d (weaken n xs x) | tt , b rewrite b = weaken d (cons d ( weaken n xs x)  (<≤ {d} {n} b)) (≤-refl d) 
insert d (weaken n {n'} xs x) | ff , b rewrite b = (weaken n (insert d xs)  (lemm0 d n n' b x)  )


{- Write code to merge two sorted lists.

   I found I needed these lemmas from the IAL:

   min-<1, min-<2, <ff, <≤

   Additionally, I found I could save myself some cases by considering these cases for two input lists:

     nil and ys

     xs and nil

     weaken and ys

     xs and weaken

     cons and cons

   This is just five cases, instead of the nine that would be required if you considered the three
   cases for the first list simultaneously with the three for the second (3 * 3 gives 9 cases).
   You will see light gray highlighting on the patterns in the cases if you do this, but that
   is ok (it is just Agda warning you that you are not breaking out all the cases explicitly).

   [20 points]
-}

lemm1 : ∀ (n  m  n' : ℕ) → n < m ≡ tt → n ≤ n' ≡ tt → n ≤ min n' m ≡ tt
lemm1 n m n' b x with keep (n' < m)
lemm1 n m n' b x | tt , e rewrite e =  x
lemm1 n m n' b x | ff , e rewrite e = (<≤ {n} {m} b)

lemm2 : ∀ (n  m  n' : ℕ) → n < m ≡ ff → n ≤ n' ≡ tt → m ≤ min n' m ≡ tt
lemm2 n  m  n'  b x with keep (n' < m)
lemm2 n  m  n'  b x | tt , e rewrite e  = (≤-trans {m} {n} {n'}  (<ff {n} {m} b) x)
lemm2 n  m  n'  b x | ff , e rewrite e = ≤-refl m 

lemm3 : ∀ (n  m  m' : ℕ) → n < m ≡ tt → m ≤ m' ≡ tt → n ≤ min n m'  ≡ tt
lemm3 n  m  m'  b x with keep (n < m')
lemm3 n m m' b x | tt , e rewrite e = ≤-refl n
lemm3 n m m' b x | ff , e rewrite e = (≤-trans {n} {m} {m'}  (<≤ {n} {m} b) x)  

lemm4 : ∀ (n  m  m' : ℕ) → n < m ≡ ff → m ≤ m' ≡ tt → m ≤ min n m' ≡ tt
lemm4 n  m  m'  b x with keep (n < m')
lemm4 n  m  m'  b x | tt , e rewrite e  = (<ff {n} {m} b)
lemm4 n  m  m'  b x | ff , e rewrite e = x

lemm5 : ∀ (n  m n'  m' : ℕ) → n < m ≡ tt → m ≤ m' ≡ tt → n ≤ n' ≡ tt → n ≤ min n' m'  ≡ tt
lemm5 n  m n'  m'  b x y  with keep (n' < m')
lemm5 n m n' m' b x y | tt , e rewrite e = y
lemm5 n m n' m' b x y | ff , e rewrite e = (≤-trans {n} {m} {m'}  (<≤ {n} {m} b) x)

lemm6 : ∀ (n  m n'  m' : ℕ) → n < m ≡ ff → m ≤ m' ≡ tt → n ≤ n' ≡ tt → m ≤ min n' m'  ≡ tt
lemm6 n  m n'  m'  b x y  with keep (n' < m')
lemm6 n m n' m' b x y | tt , e rewrite e = (≤-trans {m} {n} {n'}  (<ff {n} {m} b) y)  
lemm6 n m n' m' b x y | ff , e rewrite e = x


merge : ∀ {n : ℕ} → sortedList n → {m : ℕ} → sortedList m → sortedList (min n m)
merge {n} xs {m} ys with keep ( n < m )

merge {n} (nil n) {m} ys | tt , b rewrite b = weaken n ys ( <≤ {n} {m} b )
merge {n} (nil n) {m} ys | ff , b rewrite b = ys
merge {n} xs {m} (nil m) | tt , b rewrite b = xs
merge {n} xs {m} (nil m) | ff , b rewrite b = weaken m xs (<ff {n} {m} b)

merge {n} (weaken n {n'} xs x) {m} ys | tt , b rewrite b  = weaken n (merge xs ys) (lemm1 n m n' b x )
merge {n} (weaken n {n'} xs x) {m} ys | ff , b rewrite b = weaken m (merge xs ys) (lemm2 n  m  n'  b x)
merge {n} xs {m} (weaken m {m'} ys y) | tt , b rewrite b = weaken n (merge xs ys) (lemm3 n m m' b y )  
merge {n} xs {m} (weaken m {m'}  ys y) | ff , b rewrite b = weaken m (merge xs ys) (lemm4 n m m' b y )
merge {n} (cons n {n'} xs x) {m} (cons m {m'} ys y) | tt , b rewrite b = weaken n (merge  xs ys)   (lemm5 n m n' m' b y x)
merge {n} (cons n {n'}  xs x) {m} (cons m {m'}  ys y) | ff , b rewrite b = weaken m (merge xs ys)  (lemm6 n m n' m' b y x)
