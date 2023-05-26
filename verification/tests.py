"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        
       {
            "input": ( {"A": 150, "B": 100, "AB": 0, "O": 0}, {"A": 100, "B": 100, "AB": 50, "O": 0}),
            "answer": ( {"A": 150, "B": 100, "AB": 0, "O": 0}, {"A": 100, "B": 100, "AB": 50, "O": 0}, 250 )
        },
       {
            "input": ( {"A": 10, "B": 10, "AB": 20, "O": 20}, {"A": 20, "B": 10, "AB": 30, "O": 0}),
            "answer": ( {"A": 10, "B": 10, "AB": 20, "O": 20}, {"A": 20, "B": 10, "AB": 30, "O": 0}, 60 )
        },
        
        
       {
            "input": ( {"A": 10, "B": 0, "AB": 25, "O": 12},{"A": 0, "B": 0, "AB": 30, "O": 10}),
            "answer": ( {"A": 10, "B": 0, "AB": 25, "O": 12},{"A": 0, "B": 0, "AB": 30, "O": 10}, 40 )
        },
        {
            "input": ( {"A": 120, "B": 40, "AB": 20, "O": 90},{"A": 150, "B": 40, "AB": 20, "O": 60}),
            "answer": ( {"A": 120, "B": 40, "AB": 20, "O": 90},{"A": 150, "B": 40, "AB": 20, "O": 60}, 270 )
        }
        

    ],
     "Extra": [
        {
            "input": ( {"A": 10, "B": 0, "AB": 25, "O": 5},{"A": 0, "B": 0, "AB": 30, "O": 10}),
            "answer": ( {"A": 10, "B": 0, "AB": 25, "O": 5},{"A": 0, "B": 0, "AB": 30, "O": 10}, 35 )
        },
        {
            "input": ( {"A": 120, "B": 40, "AB": 20, "O": 90},{"A": 150, "B": 40, "AB": 20, "O": 60}),
            "answer": ( {"A": 120, "B": 40, "AB": 20, "O": 90},{"A": 150, "B": 40, "AB": 20, "O": 60}, 270 )
        },
        {
            "input": ( {"A": 100, "B": 100, "AB": 100, "O": 104},{"A": 101, "B": 101, "AB": 101, "O": 101}),
            "answer": ( {"A": 100, "B": 100, "AB": 100, "O": 104},{"A": 101, "B": 101, "AB": 101, "O": 101}, 404 )
        },   
       {
            "input": ( {"A": 12, "B": 8, "AB": 5, "O": 20},{"A": 10, "B": 5, "AB": 20, "O": 10}),
            "answer": ( {"A": 12, "B": 8, "AB": 5, "O": 20},{"A": 10, "B": 5, "AB": 20, "O": 10}, 45 )
        },   
                 {
            "input": ( {"A": 32, "B": 17, "AB": 20, "O": 28},{"A": 28, "B": 13, "AB": 37, "O": 24}),
            "answer": ({"A": 32, "B": 17, "AB": 20, "O": 28},{"A": 28, "B": 13, "AB": 37, "O": 24}, 97 )
        }, 
       {
            "input": ( {"A": 15, "B": 18, "AB": 5, "O": 20},{"A": 10, "B": 5, "AB": 20, "O": 10}),
            "answer": ( {"A": 15, "B": 18, "AB": 5, "O": 20},{"A": 10, "B": 5, "AB": 20, "O": 10}, 45 )
        },      
    ]
    
    
}

