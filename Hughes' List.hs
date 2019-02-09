-- https://www.codewars.com/kata/hughes-list/train/haskell
module HughesList where

import Data.Monoid
import Data.Function (on)

newtype Hughes a = Hughes ([a] -> [a])

runHughes :: Hughes a -> [a]
runHughes (Hughes k) = k []


mkHughes :: [a] -> Hughes a
-- mkHughes = Hughes . const 
mkHughes x = Hughes (x++)
------------------------------------------------------------

consDumb :: a -> Hughes a -> Hughes a
consDumb a h = mkHughes (a : runHughes h)

cons :: a -> Hughes a -> Hughes a
cons a (Hughes h) = Hughes $ (a:) . h


------------------------------------------------------------

appendDumb :: Hughes a -> Hughes a -> Hughes a
appendDumb a b = mkHughes (runHughes a ++ runHughes b)

instance Monoid (Hughes a) where
  mempty = mkHughes []
  -- mappend a = mkHughes . on (++) runHughes a
  mappend (Hughes ha) (Hughes hb) = Hughes $ ha . hb
------------------------------------------------------------

snocDumb :: Hughes a -> a -> Hughes a
snocDumb l a = mkHughes (runHughes l ++ [a])

snoc :: Hughes a -> a -> Hughes a
snoc l = (l <>) . flip cons mempty
