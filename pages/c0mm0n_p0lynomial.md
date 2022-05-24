---
title: Author Writeup for challenge I made in pwned3
summary: Writeups for some of my challenges in pwned
date: 2022-03-13
---

# c0mm0n_polynomial



Look at edwards curve Doubling formula on wikipedia 

https://en.wikipedia.org/wiki/Edwards_curve

<img src="https://cdn.discordapp.com/attachments/668542758365167669/952262971063689246/unknown.png" alt="wiki" /> 

Notice the first formula for doubling, 

$$
(x,y)+(x,y) = \left(\frac{2 xy}{1+dx^2y^2},\frac{y^2-x^2}{1-dx^2y^2} \right)
$$
The equation of edward's curve is given by,

$$
x^2+y^2=1+dx^2y^2
$$
We can rearrange this in terms, and put it in terms of $y^2$, i.e.

$$
y^2 - dx^2y^2=1-x^2
$$ 
$$ y^2 (1-dx^2)=(1-x^2) 
$$
$$ y^2 = \frac{(1-x^2)}{(1-dx^2)}
$$

So, how do we use this fact and solve this challenge? Notice, in `y` coordinate of the doubling formula we can substitute `y^2` in terms of `x` 
$$
y3=\frac{y^2-x^2}{1-dx^2y^2} 
$$
can be subbed as,
$$
\\ =\frac{\frac{(1-x^2)}{(1-dx^2)}-x^2}{1-dx^2\frac{(1-x^2)}{(1-dx^2)}}
$$ Moving everything around ( cross multiply, cancel common denominator etc), 

we can cancel the denominator and we get,

$$
\\ = \frac{dx^4-2x^2+1}{dx^4-2dx^2+1} 
$$
Will let the reader, check if this is true :)


So, what now? Remember `x` term is our message, so the intuition would be to solve it like equations

We are given `(x3,y3)`,  and `ciphertext`, lets look at all the equations and inspect them,
$$
y3 =\frac{dx^4-2x^2+1}{dx^4-2dx^2+1} 
$$ $$ c \equiv x^e\mod{n}
$$
where y3, is also in `mod n`. Anyway, if you look at it long enough you see that, this is basically the same as a `Franklin Reiter Related Message Attack`, i.e. they have a common polynomial `x` , hence, we can apply that attack here with some sage magic :). More on https://crypto.stackexchange.com/questions/30884/help-understanding-basic-franklin-reiter-related-message-attack .

The solve script in sage.... 

```

python
from Crypto.Util.number import *

n = 103996268785200597457400054657729976413060151228977338033643391003930647287768302869515197371901097035736501990272694915868170023537750164639401037015764843455974706668319481494480032025455755226301139490448389949897443408666069902494269114739081140535251929978733427054991169727296826771967474827868547926753

c1 = 50384969070740404863016672328984593574289561529482152745370590028448590076109868226096410422105807215032905607175444240659677097580901585202465946360552659533029029686350262553497155871769901222443595160656700977130087396999606679369271433536396834725391010788795012488308267220543391304550666066697652451811

d = 57525843535123041084333913603327980270069361310368904830328939245698964243435432838076870244867137017620684223775331018859077619960456875931333770559510843466612129337712117386122649331258312638608455155834592245819111894206453079271124330917981044167074042788007540256753216080225662492460329902370334373027

qx,qy = (92082107658055266733484033039832338851695904419137924549484599318310389538964753291832660712623529326634127142651680562415187106205249397744538318875571763140147435698552195111134720885082388679098105902809861174761072030316157142356434712239005182578684758822320763218266138477574022576715256817853678094615, 62722135743895550625323645931932423111233681829594986621564570752057592715824454259484770375322114914527122848902670818204861925243607382403459876987070947881516627693822846146782611939645098547243273788291322781461474139053266840644787762705342190464319063929249520483312574432320637099599676545420279531195)

P.<x> = PolynomialRing(Zmod(n),implementation="NTL")
f= x^e-int(c1)
g = qy*(d*x^4-2*d*x^2+1)-(d*x^4-2*x^2+1)
pgcd = lambda g1, g2: g1.monic() if not g2 else pgcd(g2, g1%g2)
print(long_to_bytes(-pgcd(f, g).coefficients()[0]))
```

