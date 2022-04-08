import Data.Gi.Base
import qualified GI.Gtk as Gtk


help_0 :: String -> String -> Float
help_0 height weight = ((read weight) / ((read height) ** 2  ) ) * 703


help_1 :: Float -> String
help_1 n = 
        if ( (n > 18.5) && (n < 24.9)) 
            then "normal bmi"
        else if (n < 18.5) 
            then "under weight bmi"
        else "overweight or obese bmi"


main = do
    putStrLn("please enter height in inches")
    height <- getLine
    putStrLn("please enter weight in pounds")
    weight <- getLine 
    putStrLn("Your bmi is " ++ (show (help_0 height weight)) ++ ". which is a(n) " ++ help_1 (help_0 height weight) ++ ".")
