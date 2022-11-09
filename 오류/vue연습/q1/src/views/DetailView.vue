<template>
  <div>
    <h1>상세페이지</h1>
    <p>글 번호 : {{ article?.id }}</p>
    <p>글 제목 : {{ article?.title }}</p>
    <p>글 내용 : {{ article?.content }}</p>
    <button @click="deleteArticle">삭제</button><br>
    <router-link :to="{name: 'article'}">뒤로가기</router-link>
  </div>
</template>

<script>
export default {
    name:'DetailView',
    data() {
        return {
            article: null,
        }
    },
    computed: {
        articles() {
            return this.$store.state.articles
        },
    },
    methods: {
        getArticleById() {
            const id = this.$route.params.id
            for (const article of this.articles) {
                if(article.id === Number(id)) {
                    // Number는 형태 변환을 위해서 사용한 도구이다.
                    this.article = article
                    break
                }
                if(!this.article){
                    this.$router.push({name: 'NotFound404'})
                }
            }
        },
        deleteArticle(){
            this.$store.commit('DELETE_ARTICLE',this.article.id)
            this.$router.push({name:'article'})
        },
    },
    created() {
        this.getArticleById(this.$route.params.id)
        },
    
    
}
</script>

<style>

</style>