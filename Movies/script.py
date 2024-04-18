import csv
from ratings.models import Movie

# Specify the path to your CSV file
csv_file_path = 'MovieRating/Movies/ratings/movies.csv'

# Open the CSV file for reading
with open(csv_file_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Iterate over each row in the CSV file
    for row in reader:
        # Create a new Movie object for each row
        movie = Movie.objects.create(
            title=row['Title'],
            release_year=row['Release Year'],
            # Add more fields as needed
        )
        
        # Save the movie object to the database
        movie.save()

print("Import completed successfully.")