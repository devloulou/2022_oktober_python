"""
MINDENKI REGISZTRÁLJON FEL A GITHUBRA


git - az egy verziókezelő rendszer

Miért van erre szükség?
Az életben előfordul, hogy több fejlesztő ugyan azt a kódbázist fejleszti, amiből
rengeteget hiba bekövetkezhet
Azt akarod, hogy minden változtatás jól elkülöníthető legyen ->ha hiba van, csak az
adott, hibás változtatást kell visszavonni

Könyebb így tesztelni
A verziókezelés egy alapvető szükség a szoftverfejlesztésben

flow:
létrehozom az úőj filet -> untracked
stagelem az untracked filet/file-okat -> staged állapot
jóváhagyom a stagelt módosítást -> commit -> ez az az időpillanat, ami a módosítás jóváhagyott pillanata
    commit esetében szükség van egy commit message-re -> dokumentációs jelentősége van

console:

git kezelté tenni a kódomat: git init
untracked állapot stagelése: git add . -> minden file-t, ami untracked
                            git add file_neve - > csak a megnevezett file-t stageled
commit: git commit -m "ide írod a commit message"

git statusok:
untracked állapot - még nincs verzió kezelve
staged állapot - git kezelés első állapota -> ezt már a git számára "véglegesíteni lehet"


branchek egyesítése: merge

ha csapatban dolgozol KERÜLD A MASTERRA VALÓ KÖZVETLEN COMMITOT
"""