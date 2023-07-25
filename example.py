import tkinter as tk

# Static list of search results (replace this with your own search logic)
search_results = [
    "Result 1",
    "Result 2",
    "Result 3",
    "Result 4",
    "Result 5",
]

def search():
    query = entry.get()
    # Perform the search here (you can replace this with your own search logic)
    # For this example, we'll just filter the results based on the query
    filtered_results = [result for result in search_results if query.lower() in result.lower()]
    
    # Clear the existing results
    results_text.delete(1.0, tk.END)

    if filtered_results:
        # Display the search results
        for result in filtered_results:
            results_text.insert(tk.END, f"- {result}\n")
    else:
        results_text.insert(tk.END, "No results found.")

# Create the main application window
root = tk.Tk()
root.title("Search Engine")

# Create and place the search input widget
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Create and place the search button
search_button = tk.Button(root, text="Search", command=search)
search_button.pack()

# Create and place the text widget to display the search results
results_text = tk.Text(root, wrap=tk.WORD, width=50, height=10)
results_text.pack(pady=10)

# Start the main event loop
root.mainloop()
