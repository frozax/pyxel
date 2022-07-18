def calcul_bien_et_mal_places(base, reference):
    assert len(base.couleurs) == len(reference.couleurs), "should have same number of colors"
    nb_cols = len(base.couleurs)
    bien_places = [False] * nb_cols
    mal_places = [False] * nb_cols
    # list des couleurs deja traités dans la ref
    deja_traite = [False] * nb_cols
    # d'abord les bien places
    for ibase, colbase in enumerate(base.couleurs):
        if reference.couleurs[ibase] == colbase:
            bien_places[ibase] = True
            deja_traite[ibase] = True
    # puis les mal places
    for ibase, colbase in enumerate(base.couleurs):
        for iref, colref in enumerate(reference.couleurs):
            if deja_traite[iref]:
                continue
            # regarde que les mal placees
            if iref == ibase:
                continue
            # ignore case deja bien placées
            if colbase == colref:
                deja_traite[iref] = True
                mal_places[ibase] = True

    print(bien_places, mal_places)
    base.bien_places = len([a for a in bien_places if a])
    base.mal_places = len([a for a in mal_places if a])
    