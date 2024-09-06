// 버튼 요소 가져오기
const toggleButton = document.getElementById('darkmode_btn');

// 클릭 이벤트 추가
toggleButton.addEventListener('click', () => {
    // 다크모드 클래스 토글
    document.body.classList.toggle('dark-mode');
});