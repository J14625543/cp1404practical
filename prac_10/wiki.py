import wikipedia


def wikipedia_lookup():
    """A simple program to look up and display Wikipedia page information."""
    print("=== Wikipedia Lookup Tool ===")
    print("Type a topic to search (press Enter to exit).")

    keep_running = True

    while keep_running:
        query = input("\nSearch term: ").strip()

        if query == "":
            print("Exiting program. Goodbye!")
            keep_running = False
            continue

        try:
            # Retrieve related search results
            search_results = wikipedia.search(query)

            # Fetch the exact page with auto_suggest turned off
            selected_page = wikipedia.page(query, auto_suggest=False)

            # Display page information
            print(f"\nTitle: {selected_page.title}")
            print(f"Summary: {selected_page.summary}")
            print(f"URL: {selected_page.url}")

        except wikipedia.exceptions.DisambiguationError as err:
            # When multiple possible results exist
            print("Your search is too broad. Try one of these suggestions:")
            for option in err.options[:10]:
                print(f"- {option}")

        except wikipedia.exceptions.PageError:
            # When the page does not exist
            print(f'No page found for "{query}". Please try another search.')

        except Exception as err:
            # Handle unexpected errors
            print(f"Unexpected error: {err}")


if __name__ == "__main__":
    wikipedia_lookup()

