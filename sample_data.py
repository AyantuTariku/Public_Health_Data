 
disease = input("Enter a disease (Malaria, Tuberculosis, HIV): ").strip().lower()

if disease == "malaria":
    print("Disease: Malaria")
    print("Number of cases: 120")
    print("Region: Oromia")

elif disease == "tuberculosis":
    print("Disease: Tuberculosis")
    print("Number of cases: 85")
    print("Region: Amhara")

elif disease == "hiv":
    print("Disease: HIV")
    print("Number of cases: 60")
    print("Region: Sidama")

else:
    print("Disease not found in the sample data.")
