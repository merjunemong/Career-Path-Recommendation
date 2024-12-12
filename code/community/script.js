document.addEventListener("DOMContentLoaded", () => {
  const postsDiv = document.getElementById("posts");

  loadPosts();

  function loadPosts() {
    const posts = JSON.parse(localStorage.getItem("posts")) || [];
    displayPosts(posts);
  }

  function displayPosts(posts) {
    if (posts.length === 0) {
      postsDiv.innerHTML = "<p>등록된 게시글이 없습니다.</p>";
      return;
    }
    postsDiv.innerHTML = "";
    posts.forEach((post, index) => {
      const postDiv = document.createElement("div");
      postDiv.classList.add("post");
      postDiv.innerHTML = `
              <h3><a href="post.html?postId=${index}">${post.title}</a></h3>
          `;
      postsDiv.appendChild(postDiv);
    });
  }
});
