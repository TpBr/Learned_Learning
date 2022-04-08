module natThms where

open import lib

-- this function divides a natural number by 2, dropping any remainder
div2 : ℕ → ℕ
div2 0 = 0
div2 1 = 0
div2 (suc (suc x)) = suc (div2 x)

div2-double : ∀(x : ℕ) → (div2 (x * 2)) ≡ x
div2-double 0  = refl
div2-double (suc x)  rewrite div2-double x = refl

{- Hint: consider the same cases as in the definition of div2: 0, 1, (suc (suc x)).
   The case for 1 is impossible, so you can just drop that case or use the 
   absurd pattern for the proof of is-even 1 ≡ tt. -}
div2-even : ∀(x : ℕ) → is-even x ≡ tt → div2 x ≡ div2 (suc x)
div2-even 0 b = refl
div2-even (suc (suc x)) b rewrite div2-even x b = refl

-- same hint as for div2-even, except now the 0 case is impossible
div2-odd : ∀(x : ℕ) → is-odd x ≡ tt → div2 (suc x) ≡ suc (div2 x)
div2-odd 1 b = refl
div2-odd (suc (suc a)) b rewrite div2-odd a b  = refl

{- hint: do *not* do induction on x.  Look at the definitions of square and pow. 
   There are lemmas about multiplication in the IAL that will help you (nat-thms.agda). -}
square-square : ∀(x : ℕ) → square (square x) ≡ x pow 4
square-square a rewrite *distribr a a 1 | *assoc a a 1 | *assoc a a ( a * a * 1) | *assoc ( a * a )  ( a * a ) 1 = sym *1

