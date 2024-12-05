import  streamlit as st

st.title('Groups: Fields and Modules, An Algebraic review of DeepLearning')

abstract,contents, acknows=st.tabs(['Abstract','Contents','Acknowledgments'])

# Abstract Tab
abstract.write('''
## Abstract
''')
abstract.write('''
FTF, this topic is a summary on my graduate algebra courses, so I will directly state the theorems, eg Syllow, as facts without the proofs.
In addition, it is also my revision of my studies on structures of deep learning networks such as, and mainly on GPTs.
I hope this revision will explain why matrices works in terms of machines' understanding the real worlds.
these pages are just chilled-out chatting, so I will only be serious on the maths proofs that I given, the remaining parts are just my thoughts, 
maybe proof-less, or even wrong, but I think its funny and maybe true, I'm happy if you point those out.
this is also sort of open-source 'project?'-ish thing, written with streamlit.\n
Feel free to do PRs or fork those and 'fix my bugs'!
''')

# Contents Tab
contents.write(
    '''
    ## an sketch of contents
    
    ### Groups: An introduction
    #### Definition
    #### examples and presentations
    #### quotient groups and finiteness
    #### theorems and lemmas
    
    ### Fields and Linear Spaces
    #### introduction of fields 
    ##### definitions
    ##### rational extension
    #### finite Fields and cyclic groups
    #### norms, metrics, and completeness
    #### p(rime)-adic fields and n-adic rings (may omitted)
    #### connectivity
    #### complex Linear Spaces
    #### groups in Linear Spaces
     
    
    ### Groups and Linear Spaces
    #### representation
    ##### definitions 
    ##### ($\mathbb{Z}$,+),and a representation of $C^{\infty}$
    
    ### Modules and morphisms
    #### Schur and Maschke 
    #### Charateristics 
    ##### inner-products and Orthogonalities
    ##### 1d reps and DFT
          
    '''

)

acknows.write(
    '''
    ## Acknowledgements
    updating...
    '''
)

