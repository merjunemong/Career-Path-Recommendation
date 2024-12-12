document.addEventListener("DOMContentLoaded", () => {
  const postId = new URLSearchParams(window.location.search).get("postId");
  const posts = JSON.parse(localStorage.getItem("posts")) || [];
  const post = posts[postId];

  const postTitle = document.getElementById("postTitle");
  const postContent = document.getElementById("postContent");
  const postDate = document.getElementById("postDate");
  const editButton = document.getElementById("editButton");
  const deleteButton = document.getElementById("deleteButton");
  const commentsDiv = document.getElementById("comments");
  const commentForm = document.getElementById("commentForm");
  const commentContent = document.getElementById("commentContent");
  const recommendButton = document.getElementById("recommendButton");
  const notRecommendButton = document.getElementById("notRecommendButton");
  const recommendCount = document.getElementById("recommendCount");
  const notRecommendCount = document.getElementById("notRecommendCount");

  if (post) {
    postTitle.innerText = post.title;
    postContent.innerText = post.content;
    postDate.innerText = post.date;

    // 추천 및 비추천 수 표시
    recommendCount.innerText = post.recommend;
    notRecommendCount.innerText = post.notRecommend;

    // 수정 버튼 링크 설정
    editButton.href = `create.html?edit=${postId}`;

    // 삭제 버튼 이벤트
    deleteButton.addEventListener("click", () => {
      if (confirm("정말 게시글을 삭제하시겠습니까?")) {
        deletePost(postId);
      }
    });

    // 추천 버튼 이벤트
    recommendButton.addEventListener("click", () => {
      post.recommend += 1;
      recommendCount.innerText = post.recommend;
      savePosts();
    });

    // 비추천 버튼 이벤트
    notRecommendButton.addEventListener("click", () => {
      post.notRecommend += 1;
      notRecommendCount.innerText = post.notRecommend;
      savePosts();
    });

    // 댓글 로드
    loadComments(post.comments);
  } else {
    document.body.innerHTML = "<p>게시글을 찾을 수 없습니다.</p>";
  }

  // 댓글 작성 이벤트
  commentForm.addEventListener("submit", (e) => {
    e.preventDefault();

    const commentText = commentContent.value.trim();
    if (commentText === "") {
      alert("댓글 내용을 입력해주세요.");
      return;
    }

    const comment = {
      content: commentText,
      date: new Date().toLocaleString(),
      recommend: 0,
      notRecommend: 0,
    };

    addComment(postId, comment);
    commentContent.value = "";
  });

  function deletePost(id) {
    posts.splice(id, 1);
    localStorage.setItem("posts", JSON.stringify(posts));
    window.location.href = "index.html";
  }

  function loadComments(comments) {
    if (!comments || comments.length === 0) {
      commentsDiv.innerHTML = "<p>등록된 댓글이 없습니다.</p>";
      return;
    }
    commentsDiv.innerHTML = "";
    comments.forEach((comment, index) => {
      const commentDiv = document.createElement("div");
      commentDiv.classList.add("comment");
      commentDiv.innerHTML = `
              <div class="comment-content">
                  <p>${comment.content}</p>
                  <small>${comment.date}</small>
              </div>
              <div class="comment-actions-container">
                  <div class="comment-recommend-section">
                      <button class="comment-recommend-button" data-index="${index}">추천 (<span class="comment-recommend-count">${comment.recommend}</span>)</button>
                      <button class="comment-not-recommend-button" data-index="${index}">비추천 (<span class="comment-not-recommend-count">${comment.notRecommend}</span>)</button>
                  </div>
                  <div class="comment-actions">
                      <button class="edit-comment-button" data-index="${index}">수정</button>
                      <button class="delete-comment-button" data-index="${index}">삭제</button>
                  </div>
              </div>
              <hr>
          `;
      commentsDiv.appendChild(commentDiv);
    });

    // 댓글 삭제 이벤트 리스너
    const deleteCommentButtons = document.querySelectorAll(
      ".delete-comment-button"
    );
    deleteCommentButtons.forEach((button) => {
      button.addEventListener("click", (e) => {
        const index = e.target.getAttribute("data-index");
        deleteComment(index);
      });
    });

    // 댓글 수정 이벤트 리스너
    const editCommentButtons = document.querySelectorAll(
      ".edit-comment-button"
    );
    editCommentButtons.forEach((button) => {
      button.addEventListener("click", (e) => {
        const index = e.target.getAttribute("data-index");
        editComment(index);
      });
    });

    // 댓글 추천 버튼 이벤트 리스너
    const commentRecommendButtons = document.querySelectorAll(
      ".comment-recommend-button"
    );
    commentRecommendButtons.forEach((button) => {
      button.addEventListener("click", (e) => {
        const index = e.target.getAttribute("data-index");
        recommendComment(index);
      });
    });

    // 댓글 비추천 버튼 이벤트 리스너
    const commentNotRecommendButtons = document.querySelectorAll(
      ".comment-not-recommend-button"
    );
    commentNotRecommendButtons.forEach((button) => {
      button.addEventListener("click", (e) => {
        const index = e.target.getAttribute("data-index");
        notRecommendComment(index);
      });
    });
  }

  function addComment(id, comment) {
    posts[id].comments.push(comment);
    localStorage.setItem("posts", JSON.stringify(posts));
    loadComments(posts[id].comments);
  }

  function deleteComment(index) {
    if (confirm("정말 댓글을 삭제하시겠습니까?")) {
      post.comments.splice(index, 1);
      savePosts();
      loadComments(post.comments);
    }
  }

  function editComment(index) {
    const newContent = prompt(
      "새로운 댓글 내용을 입력하세요:",
      post.comments[index].content
    );
    if (newContent !== null) {
      const trimmedContent = newContent.trim();
      if (trimmedContent === "") {
        alert("댓글 내용은 비워둘 수 없습니다.");
        return;
      }
      post.comments[index].content = trimmedContent;
      savePosts();
      loadComments(post.comments);
    }
  }

  function recommendComment(index) {
    post.comments[index].recommend += 1;
    savePosts();
    loadComments(post.comments);
  }

  function notRecommendComment(index) {
    post.comments[index].notRecommend += 1;
    savePosts();
    loadComments(post.comments);
  }

  function savePosts() {
    localStorage.setItem("posts", JSON.stringify(posts));
  }
});
