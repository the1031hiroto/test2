
Vue.component('todo-item', {
    props: ['todo'],
    template: '<li><img v-bind:src="todo.icon"><p>{{ todo.text }}</p></li>'
  })
  
  var app7 = new Vue({
    el: '#app-7',
    data: {
      groceryList: [
        { id: 0, icon: 'images2018/tokyo-pic/1.jpg', text: '事業戦略セッション' },
        { id: 1, icon: 'images2018/tokyo-pic/2.jpg', text: 'マーケティング戦略セッション' },
        { id: 2, icon: 'images2018/tokyo-pic/3.jpg', text: 'マーケティング戦略セッション' },
        { id: 3, icon: 'images2018/tokyo-pic/4.jpg', text: '営業戦略セッション' },
        { id: 4, icon: 'images2018/tokyo-pic/5.jpg', text: '営業戦略セッション' },
        { id: 5, icon: 'images2018/tokyo-pic/6.jpg', text: `対談セッション
パナソニック株式会社 様` },
        { id: 6, icon: 'images2018/tokyo-pic/7.jpg', text: `対談セッション
商船三井システムズ株式会社 様` },
        { id: 7, icon: 'images2018/tokyo-pic/8.jpg', text: 'ステージ' },
        { id: 8, icon: 'images2018/tokyo-pic/9.jpg', text: 'セッション会場' },
        { id: 9, icon: 'images2018/tokyo-pic/10.jpg', text: `Partner Award 授与式
株式会社大塚商会 様` },
        { id: 10, icon: 'images2018/tokyo-pic/11.jpg', text: `Partner Award 授与式
富士通株式会社 様` },
        { id: 11, icon: 'images2018/tokyo-pic/12.jpg', text: `Partner Award 授与式
日本電気株式会社 様` },
        { id: 12, icon: 'images2018/tokyo-pic/13.jpg', text: `Partner Award 授与式
東日本電信電話株式会社 様` },
        { id: 13, icon: 'images2018/tokyo-pic/14.jpg', text: `Partner Award 授与式
株式会社シーイーシー 様` },
        { id: 14, icon: 'images2018/tokyo-pic/15.jpg', text: `Partner Award 授与式
株式会社野村総合研究所 様` },
        { id: 15, icon: 'images2018/tokyo-pic/16.jpg', text: `Partner Award 授与式
伊藤忠テクノソリューションズ株式会社 様`},
        { id: 16, icon: 'images2018/tokyo-pic/17.jpg', text: `Partner Award 授与式
東日本電信電話株式会社 様` },
        { id: 17, icon: 'images2018/tokyo-pic/18.jpg', text: '受賞スピーチ' },
        { id: 18, icon: 'images2018/tokyo-pic/19.jpg', text: '懇親会' },
        { id: 19, icon: 'images2018/tokyo-pic/20.jpg', text: '懇親会' },
        { id: 20, icon: 'images2018/tokyo-pic/21.jpg', text: '懇親会' },
        { id: 21, icon: 'images2018/tokyo-pic/22.jpg', text: '懇親会' },
      ]
    }
  })
  
  var app4 = new Vue({
    el: '#app-4',
    data: {
      todos: [
        { text: 'ベストパートナー部門' },
        { text: 'ユーザープロテクション対策部門' },
        { text: 'サーバー攻撃対策部門' },
        { text: 'ベストパートナー部門' },
        { text: 'ユーザープロテクション対策部門' },
        { text: 'サーバー攻撃対策部門' },
        { text: 'ベストパートナー部門' },
        { text: 'ユーザープロテクション対策部門' },
        { text: 'サーバー攻撃対策部門' },
        { text: 'ベストパートナー部門' },
        { text: 'ユーザープロテクション対策部門' },
        { text: 'サーバー攻撃対策部門' },
        { text: 'ベストパートナー部門' },
        { text: 'ユーザープロテクション対策部門' },
        { text: 'サーバー攻撃対策部門' },
        
      ]
    }
  })
  
  var app5 = new Vue({
    el: '#app-5',
    data: {
      awards: [
        { text: 'ベストパートナー部門', img: 'images2018/tokyo-pic/31.jpg',
            text1: '株式会社大塚商会',
            text7: '代表取締役社長',
            text2: '大塚 裕司 様',
            text4: '株式会社大塚商会様は、2017年度も圧倒的な総合力で持続的な高い実績をあげられました。そしてワンストップ保守サポート「たよれーる」の独自性と高い技術力、突出した営業力を活かす「SoC部門」を設立いただきました。',
            text5: '大手・中堅向けにはMSS for DDI、SMB顧客層向けにはEasy SOC for Cloud Edgeと、幅広いお客様層をカバーし1,000社を超える展開をいただいております。今回で「15年連続」のベストパートナーの受賞です。',
            text6: ''
        },
        { text: 'クラウド/仮想化サーバ対策部門', img: 'images2018/tokyo-pic/32.jpg',
            text1: '富士通株式会社',
            text7: 'デジタルサービス部門',
            text2: '執行役員常務　副部門長',
            text3: '小田 成 様',
            text4: '富士通株式会社様は、VDI、DaaS、VMware NSXなど仮想化環境の実績を数多く持たれており、それらの環境を保護する共創ソリューションとして、3年連続でDeep SecurityにおけるNo.1の販売実績をあげられました。',
            text5: 'また、Fujitsu Cloud ServiceをはじめとするクラウドサービスでもDeep Securityをご採用いただいており、企業システムをクラウド移行するお客様を強力に支援されています。',
            text6: ''
        },
        { text: 'サイバー攻撃対策部門', img: 'images2018/tokyo-pic/33.jpg',
            text1: '日本電気株式会社',
            text7: 'システムプラットフォームBU',
            text2: '理事',
            text3: '北風 二郎 様',
            text4: '日本電気株式会社様は、昨年に続き、標的型サイバー攻撃対策としてDeep Discoveryファミリー販売売上No.1の実績をあげられました。',
            text5: 'また日本電気株式会社様は、製品のご販売のみならず、Expressサーバへのアプライアンス化、ActSecureやInfoCICといったマネージドセキュリティサービスとのセット販売、SDNとの連携ソリューションのご提供など、日本電気株式会社様ならではの付加価値の高いトータルなセキュリティソリューションをご提供いただいております。',
            text6: ''
        },
        { text: 'ユーザプロテクション対策部門', img: 'images2018/tokyo-pic/34.jpg',
            text1: '東日本電信電話株式会社',
            text7: 'ビジネス開発本部',
            text2: '理事 第三部門長',
            text3: '加藤 成晴 様',
            text4: '東日本電信電話株式会社様は、昨年よりCloud Edgeを使ったセキュリティインシデント監視・復旧支援サービス「おまかせサイバーみまもり」の提供を開始され、Cloud Edgeの売上においてNo.1の実績をあげられました。',
            text5: 'また、VBBS-Sを使ったサポートサービス「おまかせアンチウイルス」も提供開始され、中小企業のお客様に安心感を与えるトータルセキュリティサービスを推進いただいております。今後、IoTセキュリティ等新たな協業展開にも期待しております。',
            text6: ''
        },
        { text: '特別賞', img: 'images2018/tokyo-pic/37.jpg',
            text1: '伊藤忠テクノソリューションズ株式会社',
            text7: '\n執行役員',
            text2: 'ITサービスグループ　クラウドサービス本部　本部長',
            text3: '藤岡 良樹 様',
            text4: '伊藤忠テクノソリューションズ株式会社様は、当社が注力するハイブリッドクラウドセキュリティ領域に早期より取り組まれ、同社の提供されるCUBICクラウドシリーズの「CUBIC on AWS」でDeep Securityの標準搭載/展開を開始いただきました。',
            text5: 'この結果、金融業界を始めとして多岐にわたる業種Topのお客様でセキュアなハイブリッドクラウド環境が多数、採用/導入されました。今後もセキュアなハイブリッドクラウド環境を広いお客様に展開いただく事を期待しております。',
            text6: ''
        },
        { text: '特別賞', img: 'images2018/tokyo-pic/35.jpg',
            text1: '株式会社シーイーシー',
            text7: '代表取締役社長',
            text2: '田原 富士夫 様',
            text3: '',
            text4: '株式会社シーイーシー様は、トレンドマイクロが注力する全ての領域において、構築・運用サービスを早期に立ち上げ、数多くのお客様とパートナー様に展開いただきました。',
            text5: '今後は、DDIやTippingPointを始めとする月額サービスメニューの拡充や、工場向け、大学向けといった業種特化型ソリューションの訴求により更なるビジネス拡大を期待しております。',
            text6: ''
        },
        { text: '特別賞', img: 'images2018/tokyo-pic/36.jpg',
            text1: '株式会社野村総合研究所',
            text7: 'クラウドサービス本部',
            text2: '常務執行役員',
            text3: '竹本 具城 様',
            text4: '株式会社野村総合研究所様は、ビジネスコンサルティングの観点からお客様の抱える課題を包含的に解決するアプローチで当社の注力する「パブリッククラウド領域」で数多くの大型事例を獲得されました。',
            text5: '今後もセキュリティの観点だけではなくコンサルティングからシステム構築、運用監視サービスまで含めた極めて品質の高いサービスをお客様に提供いただく事でさらにビジネスを拡大いただく事を期待しております。',
            text6: ''
        },
        { text: '東日本エリア　ベストパートナー部門', img: 'images2018/tokyo-pic/38.jpg',
            text1: '東日本電信電話株式会社',
            text7: 'ビジネス開発本部',
            text2: '理事 第三部門長',
            text3: '加藤 成晴 様',
            text4: '東日本電信電話株式会社様は、東北北海道、関東甲信越地区での新規総売上No.1の実績をあげられました。',
            text5: '営業担当のみなさんが脅威動向やセキュリティ実態を学び、お客様にセキュリティ強化の必要性を訴求するシナリオ提案を徹底的に実践されるだけでなく、その成功例、失敗例を共有しながら、お客様への伝え方を工夫し続けたことが、この実績につながりました。',
            text6: '今後はSB層におけるCloud Edgeに加え、大手層への展開や、医療、自治体等の業種展開といった、新たな協業拡大に期待しております。'
        },
        
        
      ]
    }
  })