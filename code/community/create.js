document.addEventListener("DOMContentLoaded", () => {
  const postForm = document.getElementById("postForm");
  const titleInput = document.getElementById("title");
  const contentInput = document.getElementById("content");

  const queryParams = new URLSearchParams(window.location.search);
  const editPostId = queryParams.get("edit");

  if (editPostId !== null) {
    const posts = JSON.parse(localStorage.getItem("posts")) || [];
    const post = posts[editPostId];
    if (post) {
      titleInput.value = post.title;
      contentInput.value = post.content;
    }
  }

  postForm.addEventListener("submit", (e) => {
    e.preventDefault();

    const title = titleInput.value.trim();
    const content = contentInput.value.trim();

    if (title === "" || content === "") {
      alert("제목과 내용을 모두 입력해주세요.");
      return;
    }

    const post = {
      title,
      content,
      date: new Date().toLocaleString(),
      comments: [],
      recommend: 0,
      notRecommend: 0,
    };

    if (editPostId !== null) {
      updatePost(editPostId, post);
    } else {
      savePost(post);
    }

    // 폼 초기화
    titleInput.value = "";
    contentInput.value = "";

    // 홈 페이지로 돌아가기
    window.location.href = "index.html";
  });

  function savePost(post) {
    let posts = JSON.parse(localStorage.getItem("posts")) || [];
    posts.push(post);
    localStorage.setItem("posts", JSON.stringify(posts));
  }

  function updatePost(index, updatedPost) {
    let posts = JSON.parse(localStorage.getItem("posts")) || [];
    posts[index] = {
      ...posts[index], // 기존 댓글 및 추천 유지
      ...updatedPost,
    };
    localStorage.setItem("posts", JSON.stringify(posts));
  }
});
