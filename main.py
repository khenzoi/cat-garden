U

���^��@s~ddlZddlZddlZddlZddlZddlZe�d�dZee�e	d�Z
z6dZee
�dd�Z
e��Zejee
d�Zeej�ZWnYnXd	d
�Zdd�Zd
d�Zdd�Zdd�Ze�d�ee�ed�ed�ed�ed�ed�ed�e	d�Zee
�edk�r$ee
��qnVedk�r8ee
�nBedk�rLee
�n.edk�rje	d�Zee
e�ned�e��dS) �N�clearu{[0;33;40m

      ▄▄██▄▄    █  ▄█ ▀█████▄  ▄████▄    ██    
   ▄█▀▀██▀▀██  ██ ▄██   ██  ██ ██  ██ ▀██████▄ 
   ██  ██  ██ ▄████    ▄██▄█▀  ██  ██    ██  ▀ 
   ██  ██  ██ ▀████   ▀▀██▀█▄  ██  ██    ██    
   ██  ██  ██  ██ ▀██   ██  ██ ██  ██    ██    
    █  ██  █▀  ██  ▀█ ▄█████▀  ▀████▀   ▄███  
             CATS GARDEN SCRIPT
[0mz@ [3;31;40m[[0;36;40m*[3;31;40m] [1;32;40mToken >> [0;33;40mz;https://cats.garden/api/setting/bindInvitationCode/JFH47SEQ�okhttp/4.4.0��tokenz
user-agent�ZheaderscCs2d}t|�dd�}t��}|j||d�}t|j�}td�t�d|�}t|�dk�r.g}|D]}|�	dd	�}|�
|�q\td
tt|���d}	t�d|�}
|
D] }|�	dd	�}t|	�t|�}	q�td
t|	�d�t�d|�d�	dd	�}tdt|��t�d|�d�	dd	�}
tdt|
��td�dS)N�!https://cats.garden/api/cat/queryrrrz(========================================�
level":[0-9]+r�level":�zE [3;31;40m[[0;36;40m*[3;31;40m] [1;32;40mCat Count  >> [0;33;40mzoutput":[0-9]+zoutput":zE [3;31;40m[[0;36;40m*[3;31;40m] [1;32;40mCat Income >> [0;33;40mz/szuserGold":[0-9]+z
userGold":zE [3;31;40m[[0;36;40m*[3;31;40m] [1;32;40mGold       >> [0;33;40mzuserUSD":[0-9]+.[0-9]+z	userUSD":zE [3;31;40m[[0;36;40m*[3;31;40m] [1;32;40mUSD        >> [0;33;40m)�str�requests�Session�get�text�print�re�findall�len�replace�append�int)r�url�header�session�web�page�statusZ	cat_level�level�totalZ
cat_incomeZincomeZgoldZusd�r�	.\cats.py�UserInfos0
r!cCs��z�d}t|�dd�}t��}|j||d�}t|j�}g}t�d|�}t�d|�}tt|��D]2}	||	�	dd�}
||	�	d	d�}|�
|
|g�q^|D]}q�tt|��D]�}	tt|��D]�}
||	d
||
d
kr�||	d||
dkr�|	|
kr�t||	d�}t||
d�}dt|�d
t|�}t|�dd�}t��}|j||d�}t|j�}t�d|�}t|�d
kr�td�q�q�q�WqYqXqdS)NrrrrrzuserCatIdt":"[a-z0-9-]+r	r
z
userCatIdt":"r�z*https://cats.garden/api/cat/synthesisCats/�/�SUCCESSzN [3;31;40m[[0;36;40m*[3;31;40m] [1;32;40mMerge Status >> [0;33;40mSuccess)
rrr
rrrr�rangerrr�postr)rrrrrrZcatsZclvlZcId�iZcatLVLZcatID�cat�cZcat1Zcat2rrrr �merge8s>
8
r*c	Cs�z�dt|�}t|�dd�}t��}|j||d�}t|j�}t�d|�}t|�dkr�t�d|�d�dd	�}t	d
t|d�dt|��nWqt	d�YqXqdS)
Nz https://cats.garden/api/cat/buy/rrrr$rzbuyPrice":[0-9]+z
buyPrice":r
zB [3;31;40m[[0;36;40m*[3;31;40m] [1;32;40mBuy Cat >> [0;33;40mz | Price >> [0;33;40mz. [3;31;40m[[0;36;40m*[3;31;40m] REAL ERROR!�
rrr
r&rrrrrr)	r�catidrrrrrrZpricerrr �buycatcs
"r-cCs~d}t|�dd�}t��}|j||d�}t|j�}t�d|�}t|�dkrzt�d|�d�dd	�}t	d
t|d�d�dS)Nz.https://cats.garden/api/lottery/watchADForMorerrrr$rzwatchADTimesLeft":[0-9]+zwatchADTimesLeft":r
zD [3;31;40m[[0;36;40m*[3;31;40m] [1;32;40mMore SPIN >> [0;33;40mz	 + 3 Spinr+)rrrrrrrZadsrrr �morespinxs
r.cCsv�z`d}t|�dd�}t��}|j||d�}t|j�}t�d|�}t|�dk�r`t�d|�d}|�dd	�}|�d
d	�}|�dd	�}|�	d�}|d�d
d	�}t|�dk�r`d}t|�dd�}t��}|j||d�}t|j�}t�d|�}t|�dk�r&|d�dd	�}	|t
|	�}
tdt|
��nt|�d}t|�dd�}t��}|j||d�}t|j�}WqYqXqdS)Nz-https://cats.garden/api/lottery/rewardOptionsrrrzlotteryTimesLeft":[0-9]+rz\["[a-zA-Z0-9",]+\]�[r
�]�"�,zlotteryTimesLeft":z'https://cats.garden/api/lottery/start/1z
index":[0-9]+zindex":zF [3;31;40m[[0;36;40m*[3;31;40m] [1;32;40mSpin Result >> [0;33;40mz/https://cats.garden/api/lottery/watchADForPrize)
rrr
r&rrrrr�splitrrr.)rrrrrrr�optionsZspin�resultZrewardrrr �lottery�sB


r6z6 [3;31;40m[[0;36;40m1[3;31;40m] [1;32;40mSpin Farmz6 [3;31;40m[[0;36;40m2[3;31;40m] [1;32;40mSpin Rollz7 [3;31;40m[[0;36;40m3[3;31;40m] [1;32;40mAuto Mergez9 [3;31;40m[[0;36;40m4[3;31;40m] [1;32;40mAuto Buy Catz NOTE: Auto Buy Cat Need Cat IDz"==================================z= [3;31;40m[[0;36;40m*[3;31;40m] [1;32;40mEnter Choice >> �1�2�3�4z< [3;31;40m[[0;36;40m*[3;31;40m] [1;32;40mEnter CatID >> z: [3;31;40m[[0;36;40m*[3;31;40m] [1;32;40mInvalid Input)r�os�sys�timer�	threading�systemZbannerr�inputrrrrr
rr&rrrr!r*r-r.r6�choicer,�exitrrrr �<module>sL0

+.







