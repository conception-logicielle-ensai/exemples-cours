document.addEventListener("DOMContentLoaded", () => {
    const searchInput = document.getElementById("search");
    const recipeList = document.getElementById("recipe-list");
    const recipes = Array.from(recipeList.getElementsByTagName("li"));

    searchInput.addEventListener("input", () => {
        const query = searchInput.value.toLowerCase();
        recipes.forEach(li => {
            const text = li.textContent.toLowerCase();
            li.style.display = text.includes(query) ? "" : "none";
        });
    });
});