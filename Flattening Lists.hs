-- https://www.codewars.com/kata/flattening-lists/train/haskell
-- 1
module Flatten where

flatten :: [[a]] -> [a]
flatten = concat

-- 2
module Flatten where

flatten :: [[a]] -> [a]
flatten [] = []
flatten (x: xs) = x ++ flatten xs

-- 3
module Flatten where

flatten :: [[a]] -> [a]
flatten = foldl (++) []

-- 4
module Flatten where

flatten :: [[a]] -> [a]
flatten x = x >>= id
