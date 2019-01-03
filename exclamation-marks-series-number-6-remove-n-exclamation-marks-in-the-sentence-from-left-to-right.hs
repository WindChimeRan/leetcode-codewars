-- 1
module Kata (remove) where

remove :: String -> Int -> String
remove x 0 = x
remove ('!':xs) 1 = xs
remove (x:xs) 1 = x: remove xs 1
remove xs 1 = xs
remove xs n = remove (remove xs 1) (n-1)

-- 2
module Kata (remove) where

import Data.List

remove :: String -> Int -> String
remove x n = x \\ (replicate n '!')
