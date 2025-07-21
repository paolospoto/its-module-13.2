# Q11: What is wrong with the following code?
# (Tip: look carefully... 👀)


df = pd.DataFrame({  # type: ignore
    "Nome": ["Paolo", "Laura", "Michele"],
    "Età": [40, 35, 29],
    "Attivo": [True, False, True],
    "Ruolo": ["Docente", "Studente", "Tutor"]
}, index=["p1", "p2", "p3"])

print(df.loc["p2", "Ruolo"])
