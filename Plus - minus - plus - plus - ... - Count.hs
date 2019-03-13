-- https://www.codewars.com/kata/plus-minus-plus-plus-dot-dot-dot-count/train/haskell

-- 1
module SignChange (count) where

import Data.Bits (xor)

count :: (Num a,Ord a) => [a] -> Int
count []  = 0
count [x] = 0
count xs  = helper . toBool $ xs

toBool :: (Num a,Ord a) => [a] -> [Int]
toBool xs = map (\x -> if x >= 0 then 1 else 0) xs

helper :: [Int] -> Int
helper xs = sum $ map (uncurry xor) $ zip xs (tail xs)

-- 2
module SignChange (count) where
import Data.List
count :: (Num a,Ord a) => [a] -> Int
count [] = 0
count xs = pred . length . group . map (>=0) $ xs

-- others 
module SignChange (count) where

import Data.Function (on)

count :: (Num a, Ord a) => [a] -> Int
count = length . filter id . (zipWith ((/=) `on` (>= 0)) <*> tail)

-- others
module SignChange (count) where

import Data.List
import Data.Function

count :: (Num a, Ord a) => [a] -> Int
count = max 0 . pred . length . groupBy ((==) `on` (>= 0))
