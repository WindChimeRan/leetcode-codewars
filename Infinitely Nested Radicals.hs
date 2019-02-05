-- https://www.codewars.com/kata/infinitely-nested-radicals/train/haskell
-- 1
module InfinitelyNestedRadicalExpressions.Kata (fn) where

fn :: Double -> Double
fn x = sqrt $ (iterate (helper') x) !! 1000
  where helper' = helper x

helper :: Double -> Double -> Double
helper x x' = x + sqrt x'

-- 2
module InfinitelyNestedRadicalExpressions.Kata (fn) where

fn :: Double -> Double
fn x = 0.5 + sqrt (x + 0.25)
