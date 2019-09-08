module IterateN (iterateN) where

iterateN :: Int -> (a -> a) -> (a -> a)
iterateN 0 _ = id
iterateN 1 f = f
iterateN n f = (iterateN (n-1) f) . f
